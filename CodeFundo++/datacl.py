import json

data = json.load(open("data.json","r"))

json.dump([tuple((x['categories'][0]['id'], x['sources'][0]['url'])) for x in data['events']], open("data2.json","w"), indent=4)