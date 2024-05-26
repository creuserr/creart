# CreArt
Lightweight and working API for fetching artists' image artwork and other informations, powered by Spotify.

```py
# Tokens are strictly needed
token = CreArt().create_token()

# Search for the artist
artist = CreArt().search('Taylor Swift', token)

# Print the first image url
print(artist.images[0].url)
```

# Installation
Download the file [`creart.py`](https://github.com/creuserr/creart/blob/main/dist/creart.py) and import it.

```py
from creart import CreArt
```

> [!NOTE]
> This library uses the dependency `requests`.

# Documentation
## class `CreArt`
This class includes 2 subclasses and 2 methods.

#### method `create_token() -> str`
This method creates an access token that is needed when calling the method `search()`.

This has been seperated from the search method to prevent spam, as it reusable for an hour.

```py
token = CreArt().create_token()
print(token)
# "BQBMlMKBBpDJpvDUh8Cyx0qDt00z0nJeYd3428mKLJ8dAR7wl8m5HmO_DHpEPRnDioQfeF0r"
```

#### method `search(query: str, token: str) -> CreArt.Artist`

This method searches for a single artist by the query. This returns an instance of `CreArt.Artist`.

```py
# Do not forget the token!
artist = CreArt().search('Taylor Swift', token)
```

## class `CreArt.Artist`
This subclass includes 5 properties&ndash;the artist name, their genres, their follower count on Spotify, and their profile artworks.

```py
print(artist.name)
# "Taylor Swift"

print(artist.followers)
# 111026226

print(artist.genres)
# ["pop"]

images = artist.images
# Returns a list of CreArt.Image instances
```

## class `CreArt.Image`
This subclass includes 3 properties&ndash;the image url, width, and height.

```py
print(images[0].width)
# 640

print(images[0].height)
# 640

print(images[0].url)
# "https://i.scdn.co/image/ab6761610000e5ebe672b5f553298dcdccb0e676"
```
