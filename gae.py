import requests

def send_text(text):
	if text:
		resp = requests.post('http://silken-reducer-787.appspot.com/share', data = {'content': text})	
		if resp.status_code == 200:	
			jresp = resp.json()
			url = 'http://silken-reducer-787.appspot.com/share/{0}'.format(jresp['id'])
			return url
		else:
			print rest.status_code, resp.content
			return None

# usage
# gae_url = send_text(text)

