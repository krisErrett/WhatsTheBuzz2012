sentiment_list = {'limited': -1, 'suicidal': -2, 'pardon': 2, 'desirable': 2, 'protest': -2, 'lurking': -1, 'controversial': -2, 'hating': -3, 'ridiculous': -3, 'hate': -3, 'aggression': -2, 'increase': 1, 'regretted': -2, 'violate': -2, 'granting': 1, 'attracted': 1, 'poorest': -2, 'scold': -2, 'bailout': -2, 'sorry': -1, 'regrets': -2, 'struck': -1, 'misreporting': -2, 'vociferous': -1, 'lurk': -1, 'misunderstanding': -2, 'distort': -2, 'stolen': -2, 'gratification': 2, 'uncertain': -1, 'stabbed': -2, 'screaming': -2, 'courageous': 2, 'disturb': -2, 'exaggerate': -2, 'harried': -2, 'solution': 1, 'nigger': -5, 'pardons': 2, 'quaking': -2, 'monopolized': -2, 'censors': -2, 'triumph': 4, 'enjoy': 2, 'shithead': -4, 'tired': -2, 'warns': -2, 'landmark': 2, 'elegant': 2, 'fabulous': 4, 'rigorous': 3, 'emptiness': -1, 'loathing': -3, 'errors': -2, 'hide': -1, 'wreck': -2, 'desirous': 2, 'integrity': 2, 'beaten': -2, 'jocular': 2, 'poison': -2, 'victims': -3, 'endorse': 2, 'shocks': -2, 'unmotivated': -2, 'hero': 2, 'avert': -1, 'festive': 2, 'interrupting': -2, 'prblms': -2, 'active': 1, 'oversells': -2, 'kudos': 3, 'rigorously': 3, 'deferring': -1, 'postpones': -1, 'oxymoron': -1, 'launched': 1, 'stressed': -2, 'lonesome': -2, 'unwanted': -2, 'postponed': -1, 'missing': -2, 'criticism': -2, 'fantastic': 4, 'secure': 2, 'dehumanize': -2, 'cheats': -3, 'sparkling': 3, 'achievable': 1, 'cherishing': 2, 'criminals': -3, 'appeasing': 2, 'motivate': 1, 'negative': -2, 'insult': -2, 'calm': 2, 'recommend': 2, 'strike': -1, 'committing': 1, 'made-up': -1, 'supporters': 1, 'successful': 3, 'expose': -1, 'haha': 3, 'award': 3, 'hurt': -2, 'grief': -2, 'disruption': -2, 'sobering': 1, 'frenzy': -3, 'excellent': 3, 'blocking': -1, 'shoot': -1, 'disappointing': -2, 'join': 1, 'somber': -2, 'refusing': -2, 'worn': -1, 'worth': 2, 'lugubrious': -2, 'criticizing': -2, 'elegantly': 2, 'defer': -1, 'pollute': -2, 'joyous': 3, 'unjust': -2, 'laughs': 1, 'shattered': -2, 'want': 1, 'indifferent': -2, 'attract': 1, 'cocksucker': -5, 'guarantee': 1, 'farce': -1, 'puzzled': -2, 'nuts': -3, 'damage': -3, 'amazing': 4, 'uncredited': -1, 'trusted': 2, 'aching': -2, 'significance': 1, 'moron': -3, 'disappoint': -2, 'bankster': -3, 'undesirable': -2, 'badly': -3, 'uselessness': -2, 'flustered': -2, 'mess': -2, 'insecure': -2, 'lag': -1, 'loyalty': 3, 'demanding': -1, 'astoundingly': 3, 'wrong': -2, 'sentencing': -2, 'sparkles': 3, 'meaningful': 2, 'ambivalent': -1, 'complacent': -2, 'splendid': 3, 'effective': 2, 'wins': 4, 'attracts': 1, 'appreciate': 2, 'greet': 1, 'stimulate': 1, 'daredevil': 2, 'steals': -2, 'worst': -3, 'greed': -3, 'restriction': -2, 'dirtiest': -2, 'consent': 2, 'derides': -2, 'rotfl': 4, 'innovative': 2, 'responsive': 2, 'derided': -2, 'cool stuff': 3, 'welcomes': 2, 'fit': 1, 'polluters': -2, 'destroyed': -3, 'affected': -1, 'litigious': -2, 'prevented': -1, 'powerful': 2, 'safe': 1, 'supporter': 1, 'collide': -1, 'avoids': -1, 'mongering': -2, 'interrupt': -2, 'soothing': 3, 'lenient': 1, 'saddened': -2, 'gloom': -1, 'brightness': 1, 'arrested': -3, 'absolve': 2, 'dumps': -1, 'misbehave': -2, 'fitness': 1, 'entitled': 1, 'vitriolic': -3, 'luck': 3, 'interruption': -2, 'exhilarated': 3, 'celebrating': 3, 'exhilarates': 3, 'substantially': 1, 'tricked': -2, 'absolves': 2, 'contend': -1, 'touts': -2, 'pesky': -2, 'god': 1, 'lurks': -1, 'sparkle': 3, 'encourage': 2, 'loathe': -3, 'heavenly': 4, 'ranter': -3, 'sluggish': -2, 'disputed': -2, 'barrier': -2, 'threatened': -2, 'revenge': -2, 'free': 1, 'mourning': -2, 'admits': -1, 'unconvinced': -1, 'fervid': 2, 'disputes': -2, 'struggle': -2, 'boosting': 1, 'enlightened': 2, 'jubilant': 3, 'exposing': -1, 'brooding': -2, 'tolerant': 2, 'disturbed': -2, 'hopeless': -2, 'ineffectively': -2, 'enraged': -2, 'wronged': -2, 'attractions': 2, 'reassure': 1, 'lovable': 3, 'rant': -3, 'downside': -2, 'enrages': -2, 'clarity': 2, 'snubbing': -2, 'dysfunction': -2, 'cheerless': -2, 'rejects': -1, 'lawsuits': -2, 'euphoric': 4, 'euphoria': 3, 'enthral': 3, 'combats': -1, 'tragic': -2, 'inconvenient': -2, 'bitter': -2, 'lunatics': -3, 'troubled': -2, 'murder': -2, 'collapse': -2, 'conciliated': 2, 'rejected': -1, 'conciliates': 2, 'wasted': -2, 'positively': 2, 'mercy': 2, 'anxiety': -2, 'coward': -2, 'matter': 1, 'guilt': -3, 'mirth': 3, 'feeling': 1, 'slashes': -2, 'self-confident': 2, 'willingness': 2, 'pessimism': -2, 'upset': -2, 'antagonistic': -2, 'enchanted': 2, 'unconcerned': -2, 'strengthening': 2, 'forced': -1, 'strength': 2, 'reassuring': 2, 'responsible': 2, 'isolated': -1, 'impotent': -2, 'elation': 3, 'recommended': 2, 'absorbed': 1, 'laughed': 1, 'enlightens': 2, 'yucky': -2, 'indoctrinate': -2, 'unsecured': -2, 'incapable': -2, 'distracts': -2, 'visionary': 3, 'vexing': -2, 'debonair': 2, 'disjointed': -2, 'relieving': 2, 'sulking': -2, 'exonerate': 2, 'treasonous': -3, 'stupid': -2, 'lifesaver': 4, 'alarm': -2, 'flop': -2, 'solemn': -1, 'demoralized': -2, 'unsophisticated': -2, 'entertaining': 2, 'annoyed': -2, 'marvel': 3, 'pardoned': 2, 'bomb': -1, 'inspire': 2, 'hunger': -2, 'rapture': 2, 'dupe': -2, 'disturbs': -2, 'solutions': 1, 'smog': -2, 'acquit': 2, 'unemployment': -2, 'contagions': -2, 'bliss': 3, 'disgust': -3, 'enslave': -2, 'adequate': 1, 'jailed': -2, 'explorations': 1, 'criticizes': -2, 'stop': -1, 'denounce': -2, 'unfair': -2, 'frowning': -1, 'haunted': -2, 'oversell': -2, 'affronted': -1, 'interrogated': -2, 'angers': -3, 'arrests': -2, 'rescues': 2, 'idiotic': -3, 'enraging': -2, 'heavyhearted': -2, 'bad': -3, 'ban': -2, 'ruins': -2, 'ethical': 2, 'erroneous': -2, 'mandatory': -1, 'disaster': -2, 'fascinating': 3, 'thwarting': -2, 'sincerest': 2, 'horrendous': -3, 'fail': -2, 'disturbing': -2, 'resigned': -1, 'best': 3, 'clarifies': 2, 'pressured': -2, 'green wash': -3, 'meditative': 1, 'hopefully': 2, 'scorn': -2, 'lethargic': -2, 'indecisive': -2, 'lazy': -1, 'rotflol': 4, 'extend': 1, 'admiring': 3, 'felony': -3, 'restricting': -2, 'weak': -2, 'ignorance': -2, 'weary': -2, 'wtf': -4, 'debt': -2, 'improve': 2, 'pity': -2, 'protect': 1, 'accident': -2, 'disdain': -2, 'ill': -2, 'adventures': 2, 'demanded': -1, 'agonise': -3, 'indoctrinating': -2, 'monopolize': -2, 'disappears': -1, 'overstatements': -2, 'peacefully': 2, 'honouring': 2, 'irresponsible': 2, 'greenwashing': -3, 'greenwashers': -3, 'persecuting': -2, 'trust': 1, 'trickery': -2, 'parley': -1, 'condemned': -2, 'victimizing': -3, 'bothers': -2, 'confident': 2, 'startled': -2, 'interest': 1, 'jackass': -4, 'incompetent': -2, 'easy': 1, 'prosperous': 3, 'attacked': -1, 'sunshine': 2, 'excite': 3, 'wowow': 4, 'doubts': -1, 'haters': -3, 'censored': -2, 'cunt': -5, 'gracious': 3, 'distorts': -2, 'inhibit': -1, 'save': 2, 'harms': -2, 'illiteracy': -2, 'roflmao': 4, 'ugly': -3, 'slam': -2, 'stopping': -1, 'murders': -2, 'dehumanizes': -2, 'chilling': -1, 'mistake': -2, 'pessimistic': -2, 'vulnerability': -2, 'congratulation': 2, 'unresearched': -2, 'dumped': -2, 'defeated': -2, 'fakes': -3, 'shame': -2, 'dizzy': -1, 'moping': -1, 'appalling': -2, 'greenwash': -3, 'disappear': -1, 'laughting': 1, 'constrained': -2, 'vindicate': 2, 'misunderstood': -2, 'disparages': -2, 'pardoning': 2, 'damages': -3, 'disparaged': -2, 'naive': -2, 'harming': -2, 'acquitting': 2, 'blames': -2, 'misery': -2, 'tops': 2, 'evil': -3, 'greeted': 1, 'delight': 3, 'consents': 2, 'outmaneuvered': -2, 'jealous': -2, 'opportunity': 2, 'blamed': -2, 'shitty': -3, 'failing': -2, 'inspires': 2, 'greatest': 3, 'detained': -2, 'flops': -2, 'dipshit': -3, 'bereave': -2, 'appease': 2, 'sentence': -2, 'agog': 2, 'envious': -2, 'disguise': -1, 'thanks': 2, 'victim': -3, 'swears': -2, 'resigning': -1, 'yes': 1, 'convivial': 2, 'enlighten': 2, 'rapturous': 4, 'terrific': 4, 'ease': 2, 'assassination': -3, 'passive': -1, 'advanced': 1, 'beloved': 3, 'prison': -2, 'moody': -1, 'expelled': -2, 'threatens': -2, 'mocked': -2, 'insensitive': -2, 'perfects': 2, 'celebrates': 3, 'bastards': -5, 'dreams': 1, 'disadvantage': -2, 'desire': 1, 'gift': 2, 'dishonest': -2, 'disillusioned': -2, 'notorious': -2, 'honored': 2, 'drowned': -2, 'stereotype': -2, 'exonerates': 2, 'proudly': 2, 'dead': -3, 'coziness': 2, 'escape': -1, 'dear': 2, 'prick': -5, 'bore': -2, 'perfected': 2, 'enemies': -2, 'denies': -2, 'congratulate': 2, 'humor': 2, 'combat': -1, 'creative': 2, 'disheartened': -2, 'honoured': 2, 'rebellion': -2, 'denied': -2, 'pollutes': -2, 'polluter': -2, 'beating': -1, 'adorable': 3, 'bamboozle': -2, 'alarmists': -2, 'bold': 2, 'disappeared': -1, 'losing': -3, 'super': 3, 'limitation': -1, 'boycotts': -2, 'derailed': -2, 'attacks': -1, 'accepts': 1, 'choke': -2, 'blithe': 2, 'despair': -3, 'ensure': 1, 'cherish': 2, 'commit': 1, 'disqualified': -2, 'dilemma': -1, 'lied': -2, 'wasting': -2, 'prisoners': -2, 'detention': -2, 'delighted': 3, 'obscene': -2, 'thankful': 2, 'unstable': -2, 'stall': -2, 'frightened': -2, 'strangely': -1, 'annoyance': -2, 'deception': -3, 'support': 2, 'unfocused': -2, 'fight': -1, 'fucking': -4, 'war': -2, 'asset': 2, 'lowest': -1, 'starve': -2, 'underestimated': -1, 'overjoyed': 4, 'forgetful': -2, 'vitality': 3, 'failure': -2, 'underestimates': -1, 'astonished': 2, 'true': 2, 'congratulations': 2, 'injury': -2, 'invincible': 2, 'bargain': 2, 'ruined': -2, 'adore': 3, 'torturing': -4, 'faking': -3, 'propaganda': -2, 'fulfills': 2, 'promises': 1, 'looms': -1, 'disgrace': -2, 'scandalous': -3, 'sinful': -3, 'assassinations': -3, 'soothe': 3, 'promised': 1, 'sprightly': 2, 'pileup': -1, 'annoying': -2, 'shit': -4, 'oversimplification': -2, 'faithful': 3, 'eerie': -2, 'interested': 2, 'looses': -3, 'ambitious': 2, 'confusing': -2, 'misinterpreted': -2, 'denier': -2, 'scream': -2, 'assfucking': -4, 'outreach': 2, 'smile': 2, 'funerals': -1, 'died': -3, 'derail': -2, 'warn': -2, 'apologizing': -1, 'cheated': -3, 'apology': -1, 'restores': 1, 'loyal': 3, 'cheater': -3, 'optionless': -2, 'menaced': -2, 'restored': 1, 'bereaving': -2, 'remarkable': 2, 'drained': -2, 'rob': -2, 'relieve': 1, 'grateful': 3, 'battle': -1, 'polluted': -2, 'devoted': 3, 'soothed': 3, 'misread': -1, 'anticipation': 1, 'praises': 3, 'deceitful': -3, 'honoring': 2, 'disgusting': -3, 'abhorrent': -3, 'amaze': 2, 'praised': 3, 'dissatisfied': -2, 'negativity': -2, 'terror': -3, 'retreat': -1, 'fatigues': -2, 'slash': -2, 'advantage': 2, 'apeshit': -3, 'gloomy': -2, 'mourn': -2, 'fatigued': -2, 'forgiving': 1, 'feeble': -2, 'cool': 1, 'impressive': 3, 'solves': 1, 'die': -3, 'accidentally': -2, 'leave': -1, 'solved': 1, 'excellence': 3, 'denounces': -2, 'unaware': -2, 'attracting': 2, 'prevent': -1, 'brave': 2, 'fearing': -2, 'insignificant': -2, 'sigh': -2, 'obsolete': -2, 'comforting': 2, 'helpless': -2, 'irritated': -3, 'acrimonious': -3, 'rapist': -4, 'self-deluded': -2, 'curse': -1, 'jeopardy': -2, 'celebrated': 3, 'havoc': -2, 'pleased': 3, 'suspect': -1, 'shared': 1, 'falling': -1, 'axed': -1, 'supporting': 1, 'unsure': -1, 'honour': 2, 'funeral': -1, 'victimized': -3, 'envy': -1, 'deceit': -3, 'persecuted': -2, 'oversimplify': -2, 'messing up': -2, 'accomplishes': 2, 'coerced': -2, 'brilliant': 4, 'guilty': -3, 'proud': 2, 'pseudoscience': -3, 'accomplished': 2, 'ineffective': -2, 'weird': -2, 'motherfucking': -5, 'breathtaking': 5, 'charmless': -3, 'love': 3, 'humour': 2, 'hardier': 2, 'bloody': -3, 'marvelous': 3, 'betraying': -3, 'fake': -3, 'scam': -2, 'crisis': -3, 'disguising': -1, 'sympathetic': 2, 'dolorous': -2, 'cherishes': 2, 'homesick': -2, 'unimpressed': -2, 'positive': 2, 'angry': -3, 'resigns': -1, 'cherished': 2, 'loving': 2, 'conciliating': 2, 'riot': -2, 'share': 1, 'swearing': -2, 'downhearted': -2, 'wooo': 4, 'drown': -2, 'dismal': -2, 'degrade': -2, 'douche': -3, 'niggas': -5, 'pretend': -1, 'flu': -2, 'inflamed': -2, 'flagship': 2, 'wanker': -3, 'drags': -1, 'hope': 2, 'growing': 1, 'detached': -1, 'stimulating': 2, 'lighthearted': 1, 'admired': 3, 'dedicated': 2, 'lobbying': -2, 'awesome': 4, 'confused': -2, 'disbelieve': -2, 'hides': -1, 'glamourous': 3, 'chic': 2, 'provoke': -1, 'unlovable': -2, 'validated': 1, 'bankrupt': -3, 'fuming': -2, 'secured': 2, 'agonizing': -3, 'immune': 1, 'misleading': -3, 'endorsement': 2, 'dehumanizing': -2, 'secures': 2, 'unbelievable': -1, 'irrational': -1, 'critics': -2, 'averted': -1, 'disgusted': -3, 'heartbreaking': -3, 'mad': -3, 'improving': 2, 'heroes': 2, 'destructive': -3, 'fraudulence': -4, 'natural': 1, 'disconsolate': -2, 'stupidly': -2, 'amuse': 3, 'nosey': -2, 'thorny': -2, 'youthful': 2, 'deceive': -3, 'offend': -2, 'worsens': -3, 'cute': 2, 'foreclosure': -2, 'shaky': -2, 'wishing': 1, 'unacceptable': -2, 'playful': 2, 'fatalities': -3, 'cuts': -1, 'lovelies': 3, 'irresolute': -2, 'blocked': -1, 'dreading': -2, 'avid': 2, 'thank': 2, 'interesting': 2, 'torn': -2, 'troubles': -2, 'abhorred': -3, 'attraction': 2, 'swindle': -3, 'undermines': -2, 'overreacted': -2, 'lonely': -2, 'accusations': -2, 'captivated': 3, 'devastated': -2, 'reject': -1, 'sarcastic': -2, 'singleminded': -2, 'compelled': 1, 'wealthy': 2, 'bullshit': -4, 'intrigues': 1, 'undermining': -2, 'drop': -1, 'does not work': -3, 'careless': -2, 'vexation': -2, 'snubbed': -2, 'stalling': -2, 'fired': -2, 'crushing': -1, 'yeah': 1, 'breakthrough': 3, 'avoided': -1, 'disasters': -2, 'amusement': 3, 'hysteria': -3, 'giddy': -2, 'accomplish': 2, 'infuriated': -2, 'monopolizes': -2, 'irony': -1, 'agonises': -3, 'worshiped': 3, 'cancels': -1, 'infuriates': -2, 'collisions': -2, 'condemns': -2, 'trauma': -3, 'hacked': -1, 'agonised': -3, 'inaction': -2, 'phobic': -2, 'vicious': -2, 'disrespect': -2, 'felonies': -3, 'advantages': 2, 'crazier': -2, 'ominous': 3, 'care': 2, 'envies': -1, 'disguised': -1, 'collapsing': -2, 'impose': -1, 'honest': 2, 'disguises': -1, 'funky': 2, 'apologising': -1, 'winwin': 3, 'aboard': 1, 'bothersome': -2, 'outcry': -2, 'entrusted': 2, 'neglect': -2, 'blind': -1, 'suspend': -1, 'surviving': 2, 'suspended': -1, 'suing': -2, 'lags': -2, 'agonising': -3, 'ashame': -2, 'rageful': -2, 'monopolizing': -2, 'derision': -2, 'oversimplifies': -2, 'encourages': 2, 'stifled': -1, 'persecute': -2, 'legally': 1, 'oversimplified': -2, 'seduced': -1, 'hug': 2, 'appreciates': 2, 'alas': -1, 'slashed': -2, 'appreciated': 2, 'petrified': -2, 'fuking': -4, 'lmao': 4, 'depressed': -2, 'favors': 2, 'optimism': 2, 'protected': 1, 'happy': 3, 'damned': -4, 'proactive': 2, 'usefulness': 2, 'prospect': 1, 'questionable': -2, 'illness': -2, 'contentious': -2, 'jewels': 1, 'sad': -2, 'conspiracy': -3, 'distorted': -2, 'anger': -3, 'shocked': -2, 'violates': -2, 'defenseless': -2, 'destroy': -3, 'relaxed': 2, 'deniers': -2, 'pain': -2, 'oppressive': -2, 'betrayal': -3, 'suspects': -1, 'insanity': -2, 'unmatched': 1, 'cleared': 1, 'envying': -1, 'lawl': 3, "can't stand": -3, 'steadfast': 2, 'discarding': -1, 'adopt': 1, 'axe': -1, 'cheat': -3, 'infuriate': -2, 'applauding': 2, 'bright': 1, 'scoop': 3, 'aggressive': -2, 'stressor': -2, 'help': 2, 'woow': 4, 'strangled': -2, 'dick': -4, 'robs': -2, 'embittered': -2, 'crime': -3, 'dejecting': -2, 'welcomed': 2, 'tears': -2, 'travesty': -2, 'defenders': 2, 'outrage': -3, 'dreaded': -2, 'dispute': -2, 'rejoiced': 4, 'haplessness': -2, 'satisfied': 2, 'rejoices': 4, 'hailed': 2, 'consolable': 2, 'unethical': -2, 'justified': 2, 'celebrate': 3, 'astounds': 3, 'verdicts': -1, 'wrathful': -3, 'sabotage': -2, 'obliterate': -2, 'imbecile': -3, 'superb': 5, 'worried': -3, 'jokes': 2, 'overreaction': -2, 'spam': -2, 'prevents': -1, 'disparage': -2, 'worrying': -3, 'vision': 1, 'ignored': -2, 'lethargy': -2, 'imposing': -1, 'violated': -2, 'whitewash': -3, 'fucktard': -4, 'dickhead': -4, 'slashing': -2, 'ignores': -1, 'rewarded': 2, 'encouraged': 2, 'fails': -2, 'enlightening': 2, 'fascinated': 3, 'belittled': -2, 'mope': -1, 'enjoys': 2, 'moaned': -2, 'fascinates': 3, 'fearless': 2, 'pained': -2, 'killing': -3, 'blame': -2, 'jovial': 2, 'awards': 3, 'hurts': -2, 'moans': -2, 'spark': 1, 'grieved': -2, 'undermine': -2, 'frisky': 2, 'yeees': 2, 'tout': -2, 'disappointment': -2, 'protesters': -2, 'cornered': -2, 'sulky': -2, 'cancer': -1, 'smartest': 2, 'accusation': -2, 'exploit': -2, 'grants': 1, 'anti': -1, 'cancel': -1, 'perpetrators': -2, 'bizarre': -2, 'panics': -3, 'better': 2, 'screams': -2, 'punishes': -2, 'collides': -1, 'capable': 1, 'swift': 2, 'brainwashing': -3, 'jaunty': 2, 'punished': -2, 'peaceful': 2, 'ruining': -2, 'aggressions': -2, 'shortages': -2, 'blessing': 3, 'mocking': -2, 'unified': 1, 'suspected': -1, 'careful': 2, 'spirit': 1, 'colluding': -3, 'sedition': -2, 'apologised': -1, 'apologises': -1, 'cancelled': -1, 'abducted': -2, 'falsified': -3, 'huckster': -2, 'raptured': 2, 'unsupported': -2, 'sincere': 2, 'oks': 2, 'dubious': -2, 'blah': -2, 'bias': -1, 'embrace': 1, 'raptures': 2, 'ironic': -1, 'engages': 1, 'fame': 1, 'worry': -3, 'resentful': -2, 'harsh': -2, 'dithering': -2, 'granted': 1, 'underestimate': -1, 'weakness': -2, 'struggling': -2, 'favorited': 2, 'applaud': 2, 'boosted': 1, 'intimidation': -2, 'cheers': 2, 'favorites': 2, 'cheery': 3, 'weep': -2, 'complained': -2, 'longing': -1, 'charges': -2, 'amazes': 2, 'disregards': -2, 'no': -1, 'severe': -2, 'solve': 1, 'inability': -2, 'no fun': -3, 'reward': 2, 'amazed': 2, 'charged': -3, 'diffident': -2, 'robing': -2, 'exaggerating': -2, 'pissing': -3, 'kill': -3, 'greetings': 2, 'madness': -3, 'alarmist': -2, 'death': -2, 'clueless': -2, 'deceiving': -3, 'dauntless': 2, 'adventurous': 2, 'disputing': -2, 'mournful': -2, 'joyful': 3, 'starving': -2, 'kills': -3, 'reassured': 1, 'earnest': 2, 'boycotted': -2, 'accepted': 1, 'disappointed': -2, 'vague': -2, 'tremulous': -2, 'distrustful': -3, 'possessive': -2, 'terrorize': -3, 'endorses': 2, 'greeting': 1, 'miracle': 4, 'discarded': -1, 'benefit': 2, 'laughing': 1, 'dirtier': -2, 'passionate': 2, 'endorsed': 2, 'burdens': -2, 'hysterics': -3, 'exposed': -1, 'pushy': -1, 'short-sightedness': -2, 'slavery': -3, 'exposes': -1, 'intact': 2, 'gross': -2, 'noob': -2, 'douchebag': -3, 'slick': 2, 'legal': 1, 'deficit': -2, 'restoring': 1, 'apocalyptic': -2, 'destroys': -3, 'biased': -2, 'welcome': 2, 'racism': -3, 'sadden': -2, 'lmfao': 4, 'indestructible': 2, 'stereotyped': -2, 'exultantly': 3, 'disparaging': -2, 'broken': -1, 'stops': -1, 'exciting': 3, 'fondness': 2, 'joyfully': 3, 'contagion': -2, 'zealous': 2, 'smear': -2, 'cares': 2, 'favorite': 2, 'tumor': -2, 'boldly': 2, 'scornful': -2, 'masterpieces': 4, 'perturbed': -2, 'protests': -2, 'lively': 2, 'apologize': -1, 'annoys': -2, 'empathetic': 2, 'loathed': -3, 'innovates': 1, 'exonerated': 2, 'totalitarian': -2, 'betrays': -3, 'lol': 3, 'mindless': -2, 'racist': -3, 'futile': 2, 'decisive': 1, 'hysterical': -3, 'allergic': -2, 'ranters': -3, 'exasperated': 2, 'mischief': -1, 'mourns': -2, 'vested': 1, 'unsettled': -1, 'stressors': -2, 'delayed': -1, 'strikes': -1, 'sophisticated': 2, 'fascists': -2, 'promote': 1, 'irreversible': -1, 'abused': -3, 'fraud': -4, 'rage': -2, 'overreacts': -2, 'resolving': 2, 'treasure': 2, 'dirty': -2, 'abuses': -3, 'ennui': -2, 'deadlock': -2, 'agree': 1, 'affection': 3, 'illnesses': -2, 'leaked': -1, 'fright': -2, 'exhausted': -2, 'certain': 1, 'bamboozled': -2, 'censor': -2, 'tranquil': 2, 'amused': 3, 'bamboozles': -2, 'casualty': -2, 'selfish': -3, 'strikers': -2, 'pensive': -1, 'idiot': -3, 'conflictive': -2, 'short-sighted': -2, 'undermined': -2, 'fools': -2, 'dismayed': -2, 'victimize': -3, 'gaining': 2, 'obsessed': 2, 'overreact': -2, 'important': 2, 'fresh': 1, 'mourned': -2, 'applause': 2, 'apathy': -3, 'not working': -3, 'fraudulent': -4, 'doubted': -1, 'restricted': -2, 'burdening': -2, 'liar': -3, 'forget': -1, 'vile': -3, 'lack': -2, 'pique': -2, 'thoughtful': 2, 'sappy': -1, 'dreadful': -3, 'catastrophe': -3, 'opportunities': 2, 'riots': -2, 'revengeful': -2, 'robber': -2, 'remorse': -2, 'enjoying': 2, 'restrict': -2, 'distorting': -2, 'libelous': -2, 'infringement': -2, 'carefree': 1, 'saved': 2, 'crestfallen': -2, 'fan': 3, 'rape': -4, 'awful': -3, 'robed': -2, 'fag': -3, 'fad': -2, 'elated': 3, 'heaven': 2, 'misinformation': -2, 'fearful': -2, 'liars': -3, 'mistaking': -2, 'enrapture': 3, 'son-of-a-bitch': -5, 'methodical': 2, 'vivacious': 3, 'appreciating': 2, 'apologizes': -1, 'darkness': -1, 'skeptic': -2, 'disruptions': -2, 'zealots': -2, 'overload': -1, 'crush': -1, 'apologized': -1, 'undecided': -1, 'starved': -2, 'falsify': -3, 'escaping': -1, 'unprofessional': -2, 'loose': -3, 'overstatement': -2, 'motherfucker': -5, 'rigged': -1, 'disastrous': -3, 'hopelessness': -2, 'yummy': 3, 'strong': 2, 'untarnished': 2, 'tragedy': -2, 'cock': -5, 'inspired': 2, 'masterpiece': 4, 'horrified': -3, 'gleeful': 3, 'heartbroken': -3, 'murdering': -3, 'dehumanized': -2, 'whimsical': 1, 'cowardly': -2, 'snub': -2, 'deject': -2, 'irritate': -3, 'wavering': -1, 'promoting': 1, 'fraudster': -4, 'hurrah': 5, 'inquisition': -2, 'diamond': 1, 'brisk': 2, 'problem': -2, 'excuse': -1, 'broke': -1, 'retained': -1, 'doom': -2, 'glad': 3, 'unfulfilled': -2, 'offender': -2, 'sucks': -3, 'offended': -2, 'abandon': -2, 'beautiful': 3, 'stubborn': -2, 'embarrassing': -2, 'virtuous': 2, 'neglected': -2, 'accept': 1, 'boycott': -2, 'collision': -2, 'protects': 1, 'exclude': -1, 'condemn': -2, 'unappreciated': -2, 'huge': 1, 'prosecution': -1, 'obnoxious': -3, 'calms': 2, 'awkward': -2, 'terribly': -3, 'needy': -2, 'comfort': 2, 'ratified': 2, 'abhors': -3, 'hugs': 2, 'peril': -2, 'controversially': -2, 'disgraced': -2, 'questioning': -1, 'adventure': 2, 'numb': -1, 'hooliganism': -2, 'refuse': -2, 'criticize': -2, 'n00b': -2, 'spiteful': -2, 'wishes': 1, 'dread': -2, 'deafening': -1, 'pay': -1, 'pleasure': 3, 'dream': 1, 'enslaved': -2, 'heartfelt': 3, 'outraged': -3, 'committed': 1, 'hell': -4, 'smiling': 2, 'suffer': -2, 'trouble': -2, 'arrogant': -2, 'messed': -2, 'pray': 1, 'solving': 1, 'averts': -1, 'bummer': -2, 'nifty': 2, 'fool': -2, 'hurting': -2, 'good': 3, 'motivated': 2, 'abandons': -2, 'fuckface': -4, 'moaning': -2, 'belittle': -2, 'complain': -2, 'desperately': -3, 'slicker': 2, 'imprisoned': -2, 'scumbag': -4, 'bless': 2, 'stopped': -1, 'reassures': 1, 'shocking': -2, 'disorganized': -2, 'neglects': -2, 'harm': -2, 'shock': -2, 'restless': -2, 'noble': 2, 'resolute': 2, 'hard': -1, 'oppressed': -2, 'gun': -1, 'punitive': -2, 'deride': -2, 'suspecting': -1, 'seditious': -2, 'gullible': -2, 'missed': -2, 'ftw': 3, 'miss': -2, 'childish': -2, 'disquiet': -2, 'jolly': 2, 'safety': 1, 'paradise': 3, 'offline': -1, 'ass': -4, 'nervously': -2, 'warm': 1, 'bully': -2, 'pathetic': -2, 'dirt': -2, 'favored': 2, 'commits': 1, 'forgive': 1, 'pleasant': 3, 'brightest': 2, 'dire': -3, 'backed': 1, 'hapless': -2, 'heroic': 3, 'disadvantaged': -2, 'benefits': 2, 'stampede': -2, 'success': 2, 'cheering': 2, 'threat': -2, 'fallen': -2, 'top': 2, 'unhealthy': -2, 'stabs': -2, 'contender': -1, 'disregarded': -2, 'shameful': -2, 'sympathy': 2, 'humourous': 2, 'defects': -3, 'totalitarianism': -2, 'touting': -2, 'bullied': -2, 'validate': 1, 'regret': -2, 'moan': -2, 'kinder': 2, 'threatening': -2, 'revive': 2, 'wonderful': 4, 'shamed': -2, 'dumbass': -3, 'imperfect': -2, 'rescue': 2, 'relieved': 2, 'convinces': 1, 'appreciation': 2, 'luckily': 3, 'treasures': 2, 'convinced': 1, 'grace': 1, 'relieves': 1, 'kind': 2, 'picturesque': 2, 'disrespected': -2, 'grey': -1, 'spirited': 2, 'hooligans': -2, 'risks': -2, 'insulted': -2, 'restful': 2, 'sentenced': -2, 'cleaner': 2, 'motivation': 1, 'outstanding': 5, 'strengthen': 2, 'suspicious': -2, 'defect': -3, 'rewards': 2, 'sentences': -2, 'blissful': 3, 'vulnerable': -2, 'misrepresentation': -2, 'speculative': -2, 'trapped': -2, 'lackadaisical': -2, 'applauded': 2, 'aggravating': -2, 'serene': 2, 'contestable': -2, 'frauds': -4, 'approves': 2, 'inconvenience': -2, 'reach': 1, 'charm': 3, 'significant': 1, 'accepting': 1, 'boycotting': -2, 'approved': 2, 'funnier': 4, 'unequal': -1, 'squelched': -1, 'once-in-a-lifetime': 3, 'clear': 1, 'greenwasher': -3, 'clean': 2, 'hindrance': -2, 'fainthearted': -2, 'amusements': 3, 'dragged': -1, 'dodging': -2, 'stunned': -2, 'agonize': -3, 'fond': 2, 'degrades': -2, 'aghast': -2, 'dejects': -2, 'shares': 1, 'carefully': 2, 'defender': 2, 'degraded': -2, 'fine': 2, 'distressing': -2, 'aggravate': -2, 'justice': 2, 'nervous': -2, 'ruin': -2, 'unhappy': -2, 'penalty': -2, 'failed': -2, 'betray': -3, 'pretty': 1, 'indifference': -2, 'devastate': -2, 'gains': 2, 'banned': -2, 'revered': 2, 'courage': 2, 'hid': -1, 'pretending': -1, 'damnit': -4, 'frightening': -3, 'distraction': -2, 'enemy': -2, 'resolve': 2, 'contagious': -1, 'boost': 1, 'disregarding': -2, 'violent': -3, 'thwarts': -2, 'mistakes': -2, 'withdrawal': -3, 'poisoned': -2, 'courteous': 2, 'relentless': -1, 'repulsed': -2, 'insane': -2, 'cramp': -1, 'dump': -1, 'dumb': -3, 'tender': 2, 'threats': -2, 'wow': 4, 'please': 1, 'rejecting': -1, 'woo': 3, 'determined': 2, 'right direction': 3, 'silly': -1, 'piss': -4, 'cancelling': -1, 'vindicated': 2, 'hardship': -2, 'fidgety': -2, 'intimidated': -2, 'persecutes': -2, 'unstoppable': 2, 'vindicates': 2, 'fatality': -3, 'betrayed': -3, 'intimidates': -2, 'prospects': 1, 'improved': 2, 'adores': 3, 'influential': 2, 'offending': -2, 'chastising': -3, 'timorous': -2, 'adored': 3, 'improves': 2, 'scams': -2, 'forgotten': -1, 'poverty': -1, 'cynic': -2, 'faggots': -3, 'liked': 2, 'distress': -2, 'drunk': -2, 'sweet': 2, 'stuck': -2, 'rofl': 4, 'alone': -2, 'eviction': -1, 'likes': 2, 'vindicating': 2, 'improvement': 2, 'worthless': -2, 'victimizes': -3, 'some kind': 0, 'dud': -2, 'damn': -4, 'threaten': -2, 'empty': -1, 'affectionate': 3, 'fire': -2, 'cruelty': -3, 'disruptive': -2, 'misbehaving': -2, 'demand': -1, 'gag': -2, 'poised': -2, 'loom': -1, 'misunderstands': -2, 'solid': 2, 'postponing': -1, 'straight': 1, 'cashing in': -2, 'terrorizes': -3, 'admire': 3, 'healthy': 2, 'fud': -3, 'substantial': 1, 'error': -2, 'fun': 4, 'flees': -1, 'walkouts': -2, 'costly': -2, 'hoping': 2, 'backing': 2, 'overlooked': -1, 'astound': 3, 'hoax': -2, 'obstacle': -2, 'frantic': -1, 'beautifully': 3, 'rig': -1, 'anguish': -3, 'funny': 4, 'unworthy': -2, 'stimulates': 1, 'choking': -2, 'grant': 1, 'perpetrator': -2, 'engrossed': 1, 'stimulated': 1, 'madly': -3, 'grand': 3, 'esteemed': 2, 'itchy': -2, 'conflict': -2, 'displeased': -2, 'absentees': -1, 'praising': 3, 'comprehensive': 2, 'overweight': -1, 'alert': -1, 'absolved': 2, 'haunting': 1, 'robust': 2, 'timid': -2, 'starves': -2, 'cocksuckers': -5, 'regretting': -2, 'cheer': 2, 'inspirational': 2, 'clears': 1, 'absolving': 2, 'appalled': -2, 'abilities': 2, 'exploits': -2, 'reliant': 2, 'competitive': 2, 'exonerating': 2, 'cocky': -2, 'vigilant': 3, 'useful': 2, 'praying': 1, 'cut': -1, 'hated': -3, 'eager': 2, 'questioned': -1, 'crying': -2, 'eery': -2, 'excited': 3, 'hates': -3, 'useless': -2, 'motivating': 2, 'complains': -2, 'emergency': -2, 'demands': -1, 'big': 1, 'joyless': -2, 'condemnation': -2, 'rotflmfao': 4, 'matters': 1, 'suffering': -2, 'dearly': 3, 'like': 2, 'skeptical': -2, 'worsening': -3, 'imposed': -1, 'lost': -3, 'sincerely': 2, 'ignore': -1, 'distrust': -3, 'imposes': -1, 'provoking': -1, 'vibrant': 3, 'popular': 3, 'mediocrity': -3, 'foolish': -2, 'disorder': -2, 'humorous': 2, 'goddamn': -3, 'unloved': -2, 'disinclined': -2, 'urgent': -1, 'strongest': 2, 'loser': -3, 'selfishness': -3, 'curious': 1, 'irresistible': 2, 'prosecutes': -1, 'collapses': -2, 'visioning': 1, 'warnings': -3, 'thrilled': 5, 'stingy': -2, 'prosecuted': -2, 'innovation': 1, 'apathetic': -3, 'jumpy': -1, 'swiftly': 2, 'hypocritical': -2, 'agreement': 1, 'refused': -2, 'looming': -1, 'ache': -2, 'intense': 1, 'unconfirmed': -1, 'faith': 1, 'cautious': -1, 'discontented': -2, 'worse': -3, 'exaggerated': -2, 'firing': -2, 'stricken': -2, 'greets': 1, 'hahahah': 3, 'block': -1, 'exaggerates': -2, 'abusive': -3, 'nonsense': -2, 'awaited': -1, 'piteous': -2, 'colliding': -1, 'risk': -2, 'calming': 2, 'impressed': 3, 'infuriating': -2, 'sneaky': -1, 'infected': -2, 'grave': -2, 'impresses': 3, 'bored': -2, 'insensitivity': -2, 'invite': 1, 'collapsed': -2, 'audacious': 3, 'undeserving': -2, 'delighting': 3, 'alive': 1, 'hopes': 2, 'dull': -2, 'gallantry': 3, 'redeemed': 2, 'exploration': 1, 'mature': 2, 'highlight': 2, 'validates': 1, 'wicked': -2, 'repulse': -1, 'genial': 3, 'devastating': -2, 'haunt': -1, 'warning': -3, 'denying': -2, 'disappoints': -2, 'rainy': -1, 'sullen': -2, 'paradox': -1, 'peace': 2, 'backs': 1, 'tard': -2, 'preventing': -1, 'tits': -2, 'unequaled': 2, 'mock': -2, 'nice': 3, 'smiles': 2, 'scapegoat': -2, 'energetic': 2, 'accidental': -2, 'scandals': -3, 'problems': -2, 'resign': -1, 'prepared': 1, 'helping': 2, 'drag': -1, 'smiled': 2, 'worsened': -3, 'suffers': -2, 'downcast': -2, 'rescued': 2, 'humiliated': -3, 'attacking': -1, 'impatient': -2, 'bribe': -3, 'ignorant': -2, 'menace': -2, 'avoid': -1, 'discards': -1, 'rants': -3, 'cheerful': 2, 'infatuation': 2, 'intricate': 2, 'screwed up': -3, 'spamming': -2, 'suave': 2, 'expelling': -2, 'obstinate': -2, 'helps': 2, 'excluded': -2, 'stable': 2, 'dislike': -2, 'friendly': 2, 'enslaves': -2, 'chagrined': -2, 'murderous': -3, 'torture': -4, 'slickest': 2, 'manipulated': -1, 'accuse': -2, 'abduction': -2, 'cover-up': -3, 'compassionate': 2, 'anxious': -2, 'verdict': -1, 'jerk': -3, 'comforts': 2, 'unsatisfied': -2, 'calmed': 2, 'chastise': -3, 'niggaz': -5, 'uncomfortable': -2, 'exuberant': 4, 'ardent': 1, 'manipulating': -1, 'odd': -2, 'mischiefs': -1, 'appeased': 2, 'appeases': 2, 'melancholy': -2, 'upsetting': -2, 'misgiving': -2, 'desired': 2, 'focused': 2, 'sexy': 3, 'enterprising': 1, 'irritating': -3, 'great': 3, 'engage': 1, 'survivor': 2, 'uneasy': -2, 'distressed': -2, 'haunts': -1, 'fuked': -4, 'honor': 2, 'distresses': -2, 'panicked': -3, 'danger': -2, 'win': 4, 'terrified': -3, 'apprehensive': -2, 'crazy': -2, 'offends': -2, 'hardy': 2, 'scandal': -3, 'droopy': -2, 'confidence': 2, 'cheered': 2, 'crap': -3, 'illegal': -3, 'doubt': -1, 'weeping': -2, 'bitterly': -2, 'agreeable': 2, 'noisy': -1, 'clever': 2, 'rich': 2, 'fuck': -4, 'impress': 3, 'charming': 3, 'sore': -1, 'unbelieving': -1, 'ashamed': -2, 'disabling': -1, 'duped': -2, 'annoy': -2, 'challenge': -1, 'critic': -2, 'benefitting': 2, 'walkout': -2, 'recession': -2, 'praise': 3, 'fulfill': 2, 'violence': -3, 'admires': 3, 'escapes': -1, 'effectively': 2, 'wowww': 4, 'contempt': -2, 'hesitate': -2, 'united': 1, 'daring': 2, 'despairs': -3, 'destroying': -3, 'buoyant': 2, 'rejoicing': 4, 'struggles': -2, 'humerous': 3, 'fortunate': 2, 'delay': -1, 'fearsome': -2, 'justifiably': 2, 'struggled': -2, 'comedy': 1, 'intelligent': 2, 'tension': -1, 'blocks': -1, 'incompetence': -2, 'await': -1, 'bothered': -2, 'perjury': -3, 'abuse': -3, 'fatigue': -2, 'solidarity': 2, 'criticized': -2, 'dont like': -2, 'lame': -2, 'interrupted': -2, 'trembling': -2, 'acquitted': 2, 'prays': 1, 'allow': 1, 'classy': 3, 'furious': -3, 'beauties': 3, 'widowed': -1, 'doubtful': -1, 'nasty': -3, 'boosts': 1, 'perfect': 3, 'superior': 2, 'exclusion': -1, 'glee': 3, 'winning': 4, 'revives': 2, 'stalled': -2, 'criminal': -3, 'violating': -2, 'crash': -2, 'greater': 3, 'commended': 2, 'cutting': -1, 'twat': -5, 'kiss': 2, 'terrible': -3, 'admonished': -2, 'panic': -3, 'mirthful': 3, 'expels': -2, 'trap': -1, 'incapacitated': -2, 'disregard': -2, 'promise': 1, 'cry': -1, 'thwart': -2, 'aggravates': -2, 'aggravated': -2, 'burdened': -2, 'incensed': -2, 'fraudsters': -4, 'blesses': 2, 'gallant': 3, 'chaos': -2, 'fascist': -2, 'hilarious': 2, 'postpone': -1, 'supports': 2, 'despairing': -3, 'jackasses': -4, 'shortage': -2, 'greedy': -2, 'loomed': -1, 'conflicts': -2, 'embarrass': -2, 'shrew': -4, 'scary': -2, 'hostile': -2, 'steal': -2, 'keen': 1, 'sleeplessness': -2, 'sorrowful': -2, 'scare': -2, 'distracted': -2, 'embarrasses': -2, 'pitied': -1, 'confuse': -2, 'reaches': 1, 'jesus': 1, 'embarrassed': -2, 'mocks': -2, 'bitch': -5, 'lagging': -2, 'foreclosures': -2, 'reached': 1, 'suck': -3, 'unapproved': -2, 'salient': 1, 'sadly': -2, 'cynical': -2, 'fuckers': -4, 'silencing': -1, 'attack': -1, 'exhilarating': 3, 'perfectly': 3, 'misinformed': -2, 'adopts': 1, 'interests': 1, 'craziest': -2, 'chagrin': -2, 'punish': -2, 'doomed': -2, 'apologise': -1, 'dreary': -2, 'innovate': 1, 'depressing': -2, 'applauds': 2, 'manipulation': -1, 'astounded': 3, 'loved': 3, 'glamorous': 3, 'warfare': -2, 'boring': -3, 'bother': -2, 'tortured': -4, 'swindles': -3, 'tortures': -4, 'pretends': -1, 'misunderstand': -2, 'accusing': -2, 'thwarted': -2, 'woebegone': -2, 'poisons': -2, 'comfortable': 2, 'recommends': 2, 'sincerity': 2, 'miserable': -3, 'blockbuster': 3, 'demonstration': -1, 'clearly': 1, 'bastard': -5, 'afraid': -2, 'congrats': 2, 'boastful': -2, 'battles': -1, 'provokes': -1, 'skeptics': -2, 'provoked': -1, 'asshole': -4, 'underestimating': -1, 'snubs': -2, 'alienation': -2, 'clash': -2, 'prblm': -2, 'disappointments': -2, 'harmful': -2, 'courtesy': 2, 'prisoner': -2, 'alarmed': -2, 'medal': 3, 'fervent': 2, 'fair': 2, 'deny': -2, 'enthusiastic': 3, 'stronger': 2, 'fiasco': -3, 'contemptuous': -2, 'survived': 2, 'exclusive': 2, 'chances': 2, 'sceptical': -2, 'agreed': 1, 'supported': 2, 'beatific': 3, 'fear': -2, 'darkest': -2, 'agrees': 1, 'litigation': -1, 'inspiring': 3, 'conciliate': 2, 'winner': 4, 'hopeful': 2, 'rash': -2, 'won': 3, 'fatiguing': -2, 'inferior': -2, 'indignant': -2, 'prosecute': -1, 'doubting': -1, 'harmed': -2, 'lucky': 3, 'exultant': 3, 'dodgy': -2, 'marvels': 3, 'spammers': -3, 'gray': -1, 'deceives': -3, 'shy': -1, 'dejected': -2, 'wish': 1, 'thoughtless': -2, 'deceived': -3, 'strengthened': 2, 'accuses': -2, 'humiliation': -3, 'expel': -2, 'catastrophic': -4, 'yearning': 1, 'accused': -2, 'triumphant': 4, 'desperate': -3, 'zealot': -2, 'awaits': -1, 'exploited': -2, 'wealth': 3, 'insulting': -2, 'cheaters': -3, 'invulnerable': 2, 'frustrates': -2, 'green washing': -3, 'favor': 2, 'beautify': 3, 'injustice': -2, 'horrible': -3, 'progress': 2, 'harsher': -2, 'frustrated': -2, 'subversive': -2, 'fed up': -3, 'ability': 2, 'importance': 2, 'joy': 3, 'sorrow': -2, 'regretful': -2, 'vitamin': 1, 'embarrassment': -2, 'merry': 3, 'approval': 2, 'poorer': -2, 'lawsuit': -2, 'absentee': -1, 'direful': -3, 'limits': -1, 'joke': 2, 'powerless': -2, 'fulfilled': 2, 'admit': -1, 'deriding': -2, 'safely': 1, 'glorious': 2, 'unclear': -1, 'commend': 2, 'competent': 2, 'laugh': 1, 'cynicism': -2, 'suicide': -2, 'validating': 1, 'pissed': -4, 'waste': -1, 'chastised': -3, 'perplexed': -2, 'harshest': -2, 'interrupts': -2, 'spammer': -3, 'ensuring': 1, 'tense': -2, 'chastises': -3, 'swindling': -3, 'piqued': -2, 'banish': -1, 'novel': 2, 'toothless': -2, 'abandoned': -2, 'intimidate': -2, 'irate': -3, 'promotes': 1, 'stunning': 4, 'hahaha': 3, 'promoted': 1, 'frustrating': -2, 'loathes': -3, 'agonized': -3, 'chaotic': -2, 'unintelligent': -2, 'encouragement': 2, 'respected': 2, 'optimistic': 2, 'agonizes': -3, 'whore': -4, 'lunatic': -3, 'unbiased': 2, 'maddening': -3, 'defiant': -1, 'romance': 2, 'strange': -1, 'smarter': 2, 'privileged': 2, 'difficult': -1, 'injured': -2, 'conflicting': -2, 'spiritless': -2, 'overselling': -2, 'retarded': -2, 'fucker': -4, 'bullying': -2, 'discredited': -2, 'discouraged': -2, 'fucked': -4, 'skepticism': -2, 'lobby': -2, 'expand': 1, 'destruction': -3, 'retard': -2, 'frikin': -2, 'discounted': -1, 'fascinate': 3, 'obstacles': -2, 'disoriented': -2, 'enrage': -2, 'failures': -2, 'drowns': -2, 'restore': 1, 'stout': 2, 'cried': -2, 'discord': -2, 'mumpish': -2, 'misbehaves': -2, 'mistaken': -2, 'cries': -2, 'glum': -2, 'misbehaved': -2, 'happiness': 3, 'afflicted': -1, 'generous': 2, 'terrorized': -3, 'passively': -1, 'killed': -3, 'arrest': -2, 'extends': 1, 'roflcopter': 4, 'exempt': -1, 'despondent': -3, 'indignation': -2, 'smart': 1, 'clouded': -1, 'resolved': 2, 'increased': 1, 'myth': -1, 'crushed': -2, 'virulent': -2, 'livid': -2, 'mirthfully': 3, 'burden': -2, 'resolves': 2, 'crushes': -1, 'woeful': -3, 'prominent': 2, 'loss': -3, 'racists': -3, 'helpful': 2, 'inviting': 1, 'inquisitive': 2, 'exploiting': -2, 'admitted': -1, 'warned': -2, 'nerves': -1, 'poor': -2, 'scared': -2, 'hail': 2, 'immortal': 2, 'growth': 2, 'supportive': 2, 'neglecting': -2, 'hesitant': -2, 'leak': -1, 'corpse': -1, 'anguished': -3, 'rewarding': 2, 'woohoo': 3, 'screwed': -2, 'worsen': -3, 'blurry': -2, 'benefitted': 2, 'murderer': -2, 'reaching': 1, 'hooligan': -2, 'chokes': -2, 'slut': -5, 'pressure': -1, 'uptight': -2, 'worthy': 2, 'scapegoats': -2, 'choked': -2, 'frustrate': -2, 'hiding': -1, 'gained': 2, 'inconsiderate': -2, 'visions': 1, 'freedom': 2, 'swear': -2, 'discard': -1, 'contending': -1, 'obliterated': -2, 'commitment': 2, 'screamed': -2, 'na\xefve': -2, 'badass': -3, 'acquits': 2, 'rejoice': 4, 'lagged': -2, 'indoctrinates': -2, 'awarded': 3, 'stamina': 2, 'restricts': -2, 'frustration': -2, 'indoctrinated': -2, 'relishing': 2, 'touted': -2, 'abductions': -2, 'bitches': -5, 'not good': -2, 'blaming': -2, 'admonish': -2, 'fuckhead': -4, 'gain': 2, 'contemptuously': -2, 'ha': 2, 'assets': 2, 'lovely': 3, 'glory': 2, 'protesting': -2, 'distract': -2, 'warmth': 2, 'excitement': 3, 'cruel': -3, 'convince': 1, 'delights': 3, 'gagged': -2, 'gullibility': -2, 'faggot': -3, 'strengthens': 2, 'horrific': -3, 'intimidating': -2, 'inadequate': -2, 'meaningless': -2, 'upsets': -2, 'goodness': 3, 'authority': 1, 'infatuated': 2, 'immobilized': -1, 'detain': -2, 'sick': -2, 'gallantly': 3, 'reckless': -2, 'derails': -2, 'profiteer': -2, 'ecstatic': 4, 'traumatic': -3, 'treason': -3, 'astounding': 3, 'insults': -2, 'chance': 2, 'stab': -2, 'animosity': -2, 'godsend': 4, 'inspiration': 2, 'ghost': -1, 'insipid': -2, 'bereaves': -2, 'jewel': 1, 'disconsolation': -2, 'accidents': -2, 'expands': 1, 'abhor': -3, 'bereaved': -2}
