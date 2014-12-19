import config
import clipboard
import console
import gae
import pocket		

def error(message): console.hud_alert(message, 'error')

console.show_activity()
text = clipboard.get()

if text:
	print 'Sending {0} bytes to GAE...'.format(len(text))
	gae_url = gae.send_text(text)
	
	if gae_url:
		print 'Obtained URL {0} from GAE.'.format(gae_url)
		print 'Sending URL to Pocket...'
		if pocket.add_url(config.consumer_key, config.access_token, gae_url):
			console.hud_alert('Done')
		else:
			error('Error sending text to Pocket!')
	else:
		error('Error sending text to GAE!')
else:
	error('No text in clipboard!')

console.hide_activity()
