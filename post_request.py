import httplib2, urllib
import json
import base64

def create_base_64_bearer_token(keys):
    print('here')
    consumer_key = keys['consumer_key']
    consumer_secret = keys['consumer_secret']
    keys['base_64_bearer_token'] = base64.b64encode(bytearray(consumer_key+":"+consumer_secret, 'utf-8'))
    keys['base_64_bearer_token'] = "Basic " + keys['base_64_bearer_token'].decode('utf-8')
    return keys

def get_tweet(id):
    with open('api_keys.json') as f:
        keys = json.load(f)
    if not 'base_64_bearer_token' in keys:
        keys = create_base_64_bearer_token(keys)
        print(keys['base_64_bearer_token'])
    if not 'http_request_auth' in keys:
        params = urllib.parse.urlencode({"grant_type":"client_credentials"})
        headers = {"Content-type": "application/x-www-form-urlencoded",
                    "Accept": "gzip", "Authorization": keys['base_64_bearer_token']}
        conn = httplib2.Http()
        response, content = conn.request("https://api.twitter.com/oauth2/token", "POST", headers=headers, body=params)
        content = json.loads(content.decode("utf-8"))
        keys['http_request_auth'] = "Bearer " + content['access_token']
        print(keys['http_request_auth'])

    headers = {"Authorization": keys['http_request_auth']}
    conn = httplib2.Http()
    url = "https://api.twitter.com/1.1/statuses/lookup.json?id="+id
    response, content = conn.request(url, "GET", headers=headers)
    print(response.status, response.reason)
    content = json.loads(content.decode("utf-8"))
    with open('api_keys.json', 'w') as fp:
        json.dump(keys, fp)
    return content


def get_metadata(user):
    with open(user+'_all_ids.json') as f:
        ids = json.load(f)
    contents = []
    for i in range(0, len(ids), 100):
        print("("+str(i)+"-"+str(i+100)+") 0f "+str(len(ids)))
        id = ','.join(ids[i:min(i+100, len(ids))])
        c = get_tweet(id)
        for content in c:
            saver = {}
            saver['retweet_count'] = content['retweet_count']
            saver['favorite_count'] = content['favorite_count']
            saver['text'] = content['text']
            saver['id_str'] = content['id_str']
            saver['created_at'] = content['created_at']
            contents.append(saver)
    outfile = user+"_final.json"
    with open(outfile, 'w') as fp:
        json.dump(contents, fp)