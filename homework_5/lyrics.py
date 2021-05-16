import json
import requests


song = "self control"
song = song.replace(' ', '%20')
author = 'frank ocean'
author = author.replace(' ', '%20')
song_url = 'https://some-random-api.ml/lyrics?title=' + song
panda_url = 'https://some-random-api.ml/facts/panda'
#fact = json.loads(requests.get(panda_url).content)["fact"]
data = json.loads(requests.get(song_url).content)
print('Lyrics to ' + data['title'] + ' by ' + data['author'] + ':\n\n' + data['lyrics']   )

