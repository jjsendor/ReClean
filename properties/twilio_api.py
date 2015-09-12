import staticconf
from twilio.rest import TwilioRestClient

filename = 'secret.yaml'
staticconf.YamlConfiguration(filename)

account_sid = staticconf.read('account_sid')
auth_token = staticconf.read('auth_token')
to_number = staticconf.read('to')
from_number = staticconf.read('from')

def send_text_message():
	client = TwilioRestClient(account_sid, auth_token)
	 
	message = client.messages.create(body="Please clean your pod lads!",
	    to=to_number,
	    from_=from_number)
	return message.sid