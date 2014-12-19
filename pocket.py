import sys
import requests
import json
import webbrowser

from config import consumer_key

# just put some random URL, if I get there, I know it worked
redirect_url = 'http://www.google.com/' 

def obtain_request_token():
	resp = requests.post('https://getpocket.com/v3/oauth/request', data = json.dumps({'consumer_key': consumer_key, 'redirect_uri': redirect_url}), headers = {'Content-type':'application/json', 'X-Accept':'application/json'})
	
	if resp.status_code == 200:
		jresp = resp.json()
		return jresp['code']
	else:
		return None

def continue_authorization(code):
	url = 'https://getpocket.com/auth/authorize?request_token={0}&redirect_uri={1}'.format(code, redirect_url)
	webbrowser.open(url)
	
def get_access_token(code):
	resp = requests.post('https://getpocket.com/v3/oauth/authorize', data = json.dumps({'consumer_key': consumer_key, 'code': code}), headers = {'Content-type':'application/json', 'X-Accept':'application/json'})
	if resp.status_code == 200:
		jresp = resp.json()
		return jresp['access_token']
	else:
		return None 

def add_url(consumer_key, access_token, url):
	resp = requests.post('https://getpocket.com/v3/add', data = json.dumps({'consumer_key': consumer_key, 'access_token': access_token, 'url': url}), headers = {'Content-type':'application/json', 'X-Accept':'application/json'})	
	if resp.status_code == 200:
		return True
	else:
		print resp.status_code, resp.content
		return False

# tests

#token = obtain_request_token()
#continue_authorization(token)
#access_token = get_access_token('XXXX')

#add_url(consumer_key, access_token, 'ANY URL')
