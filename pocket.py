import sys
import requests
import json
import webbrowser

from config import consumer_key

redirect_url = 'pythonista://saveToPocket/pocket?action=run&args=authorized'

def obtain_request_token():
	resp = requests.post('https://getpocket.com/v3/oauth/request', data = json.dumps({'consumer_key': consumer_key, 'redirect_uri': redirect_url}), headers = {'Content-type':'application/json', 'X-Accept':'application/json'})
	
	print resp.status_code, resp.content, resp.headers
	
	if resp.status_code == 200:
		jresp = resp.json()
		code = jresp['code']
		print code
		return code
	else:
		return None

def continue_authorization(code):
	#url = 'pocket-oauth-v1:///authorize?request_token={0}&redirect_uri={1}'.format(code, redirect_url)
	url = 'https://getpocket.com/auth/authorize?request_token={0}&redirect_uri={1}'.format(code, redirect_url)
	webbrowser.open(url)
	
def get_access_token(code):
	resp = requests.post('https://getpocket.com/v3/oauth/authorize', data = json.dumps({'consumer_key': consumer_key, 'code': code}), headers = {'Content-type':'application/json', 'X-Accept':'application/json'})
	
	print resp.status_code, resp.content
	if resp.status_code == 200:
		jresp = resp.json()
		access_token = jresp['access_token']
		return access_token
	else:
		return None 

if len(sys.argv) > 1:
	print 'authorized'
	
token = obtain_request_token()
continue_authorization(token)
