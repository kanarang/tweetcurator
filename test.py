import json
import operator

def format(user):
    dbfile = user+'_final.json'
    with open(dbfile) as data:
        db = json.load(data)
    db.sort(key=operator.itemgetter('retweet_count', 'favorite_count'), reverse=True)

    for d in db[0:100]:
        print("https://www.twitter.com/statuses/"+d['id_str'])
        print(str(d['retweet_count'])+" "+str(d['favorite_count'])+"\n\n"+d['text']+"\n")

