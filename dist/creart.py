import requests, json

class CreArt:
  class Image:
    def __init__(self, w, h, u):
      self.width = w
      self.height = h
      self.url = u
    
  class Artist:
    def __init__(self, artist):
      self.followers = artist['followers']['total']
      self.genres = artist['genres']
      self.name = artist['name']
      self.images = []
      for image in artist['images']:
        self.images.append(CreArt.Image(image['width'], image['height'], image['url']))
  
  def create_token(self):
    req = requests.get('https://open.spotify.com/get_access_token?reason=transport&productType=web_player')
    return json.loads(req.text)['accessToken']
  
  def search(self, query, token):
    h = { 'Authorization': 'Bearer ' + token }
    req = requests.get(f'https://api.spotify.com/v1/search?type=artist&q={query}&decorate_restrictions=false&best_match=true&include_external=audio&limit=1', headers=h)
    res = json.loads(req.text)['best_match']['items']
    if len(res) == 0: return
    return CreArt.Artist(res[0])
