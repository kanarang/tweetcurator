import json
import operator

def format(user, maximum=0, mode='retweets'):
    dbfile = user+'_final.json'
    with open(dbfile) as data:
        db = json.load(data)

    if(mode=='retweets'):
        db.sort(key=operator.itemgetter('retweet_count', 'favorite_count'), reverse=True)
    elif(mode=='favs'):
        db.sort(key=operator.itemgetter('favorite_count', 'retweet_count'), reverse=True)
    elif(mode=='sum'):
        db.sort(key=lambda k: k['retweet_count']+k['favorite_count'], reverse=True)
    maximum += len(db) if maximum<=0 else 0
    maximum = min(maximum, len(db))
    maximum = max(maximum, 0)
    for d in db[0:maximum]:
        print("https://www.twitter.com/statuses/"+d['id_str'])
        print(str(d['retweet_count'])+" "+str(d['favorite_count'])+"\n\n"+d['text']+"\n")

