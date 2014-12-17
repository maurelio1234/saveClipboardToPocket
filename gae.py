import requests
import clipboard
import console

def send_text_to_gae(text):
	if text:
		print len(text)
		resp = requests.post('http://silken-reducer-787.appspot.com/share', data={'content': text})
		print resp.status_code, resp.content
	
		if resp.status_code == 200:
			#console.hud_alert('done!')
		
			jresp = resp.json()
			url = 'http://silken-reducer-787.appspot.com/share/{0}'.format(jresp['id'])
			print url
		
			#import webbrowser
			#webbrowser.open(url)
			
			return url
		return None

		#todo: actually send data to pocket ;)
		
		
#text = clipboard.get()
#gae_url = send_text_to_gae()
#if gae_url:
#	send_url_to_pocket(url)

