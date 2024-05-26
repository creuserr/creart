# CreArt
Lightweight and working API for fetching artists' image artwork and other informations, powered by Spotify.

```py
# Tokens are strictly needed
token = CreArt().create_token()

# Search for the artist
artist = CreArt().search('Taylor Swift', token)

# Print the first image url
print(artist.images[0].url)

# Print the artist's genres
print(artist.genres)

# Print the artist's follower count
print(artist.followers)
```
