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
	 
	message = client.messages.create(body="""Hi Kuba,
Here's a reminder to complete your cleaning schedule. Please text back with confirmation of the completed cleaning within 72 hours. Any problems please call the office on 0800 72 72 72.

Have a great week!

The ReClean Team""",
	    to=to_number,
	    from_=from_number)
	return message.sid