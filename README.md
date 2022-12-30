# 💥MyAnimeList.py
MyAnimeList.py is an easy-to-use API wrapper library for Python.

### Features
- Connect easily to the API
- Search in the MyAnimeList Database
- Connect with **OAuth2** and handle your account and lists 

## Getting started
### Application prerequisites
Before being able to make requests to the API, you need to create an application [here](https://myanimelist.net/apiconfig). 
### Exemples
#### Without OAuth
Here is an example of a basic program using the api without the oauth.
```python
from myanimelist import Client

client = Client('YOUR CLIENT_ID')
client.search('anime', 'One Piece', limit=10)  # Return a python dictionary with the response of the request 
```
#### With OAuth
If you want to use the functions using the OAuth, you need to add it in the constructor.
A web page will then open, and ask you to connect. Once connected, you'll be redirected to a localhost server that get the token to interact with the functions.
A `keys.py` document will be then created to stock the keys. **Make sure not to post it on Git.**
The `ACCESS_TOKEN` do not last for very long, so you will probably have to refresh it with the method `.refresh()`. Once the keys are stocked in the file, the program will start without the web page opening

Here is a basic example where you can add something to your list:
```python
from myanimelist import Client

client = Client('CLIENT_ID', client_secret='CLIENT_SECRET', OAuth=True) # Web page opening if first launch
client.add('anime', 21, status='plan_to_watch')  # Set anime with ID 21 (One Piece) to plan_to_watch
```