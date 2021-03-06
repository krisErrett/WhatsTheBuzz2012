from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
import os
from django.utils import simplejson as json # help -> http://stackoverflow.com/questions/1171584/how-can-i-parse-json-in-google-app-engine
import string
from sentiment import sentiment_list

# date model
class Tweet(db.Model):
    created_at = db.TextProperty()
    from_user = db.TextProperty()
    from_user_id = db.IntegerProperty()
    from_user_id_str = db.TextProperty()
    from_user_name = db.TextProperty()
    geo = db.GeoPtProperty()
    id = db.IntegerProperty() 
    id_str = db.TextProperty()
    iso_language_code = db.TextProperty()
    metadata = db.TextProperty()
    profile_image_url = db.LinkProperty()
    profile_image_url_https = db.LinkProperty()
    source = db.TextProperty()
    to_user = db.TextProperty()
    to_user_id = db.IntegerProperty()
    to_user_id_str = db.TextProperty()
    to_user_name = db.TextProperty()
    text = db.TextProperty()

symbol_dict = {'!':'%21', '"':'%22', '#':'%23', '$':'%24', '%':'%25', '&':'%26', '(':'%28', ')':'%29', '*':'%2A', '+':'%2B', ',':'%2C', '-':'%2D', '.':'%2E', '/':'%2F'}


class TemplatedPage(webapp.RequestHandler):
    """Base class for templatized handlers."""
    def write_template(self, values):
        """Write out the template with the same name as the class name."""
        path = os.path.join(os.path.dirname(__file__), 'templates/' + self.__class__.__name__ + '.html')  # need to add 'templates',
        self.response.out.write(template.render(path, values))

class MainPage(TemplatedPage):
    def get(self):
        template_values = {           
        }
        self.write_template(template_values)
        
class ResultPage(TemplatedPage):
    def post(self):
        search = self.request.get('search')
        # for URL encoding
        search1 = search
        for c in search1:
            if c in symbol_dict.keys():
                search1 = string.replace(search1, c, symbol_dict[c])             
        search1 = string.replace(search1, ' ', '%20')
        url = 'http://search.twitter.com/search.json?q=' + search1 + '&iso_language_code=en&page=10&rpp=100'
        
        results = urlfetch.fetch(url)
        results = json.loads(results.content)
        results = results['results']
        
        mem_list = []

        tweet_list = []
        for result in results:
            tweet = Tweet()
            tweet.created_at = result['created_at']
            tweet.from_user = result['from_user']
            tweet.from_user_id = result['from_user_id']
            tweet.from_user_id_str = result['from_user_id_str']
            if result['geo']:
                tweet.geo = ', '.join(str(coords) for coords in result['geo']['coordinates'])            
            tweet.id = result['id']
            tweet.id_str = result['id_str']
            tweet.iso_language_code = result['iso_language_code']
            tweet.metadata = str(result['metadata'])
            tweet.profile_image_url = result['profile_image_url']
            tweet.profile_image_url_https = result['profile_image_url_https']
            tweet.source = result['source']
            tweet.text = result['text']
            tweet_list.append(tweet.text)
            tweet.to_user = result['to_user']
            tweet.to_user_id = result['to_user_id']
            tweet.to_user_id_str = result['to_user_id_str']
            tweet.to_user_name = result['to_user_name']
            if not mem_list:
                mem_list.append(tweet.from_user)
                mem_list.append(tweet.profile_image_url)
            #tweet.put() # store Tweet in datastore
        
        sentiment_points = 0
        hits = 0            
        for tweet in tweet_list:
            sentence = tweet.split()
            for word in sentence:
                sentiment_points = sentiment_points + sentiment_list.get(word.lower(),0)
                if word.lower() in sentiment_list.keys():                    
                    hits = hits + 1
           
        sentiment_score = float(sentiment_points) / float(hits)
        mem_list[0:0] = [sentiment_score] # makes buzz first list element
        
        mem = memcache.Client()
        
        config = mem.get('config')
        if config is None:
            config = [search]
            mem.add('config',config)
        elif search not in config:
            config.append(search)   
            mem.set('config', config)
            mem.add(search, mem_list)
        else:
            mem.set(search, mem_list)
        
        buzz_dict = {}    
        config = mem.get('config')
        for key in config:
            value = mem.get(key)
            if value is None:
                config.remove(key)
                mem.set('config', config)
            else:
                buzz_dict[key] = value
               
            
        # for memcache http://stackoverflow.com/questions/3611830/how-do-i-return-all-memcached-values-in-google-app-engineS    
            
        template_values = {
            'tweet_list':tweet_list,
            'search':search,
            'sentiment_score':sentiment_score,
            'buzz_dict':buzz_dict  
        }
        self.write_template(template_values)
                        
''' registers the URL with the responsible classes'''
application = webapp.WSGIApplication([('/', MainPage),
                                      ('/ResultPage', ResultPage)],                                                                           
                                      debug=True)

''' registers the wsgi application to run'''
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()