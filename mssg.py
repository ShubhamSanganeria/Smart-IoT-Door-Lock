from twilio.rest import Client
from cred import *
def send_mssg():
	client=Client(acc_ssid,auth_code)
	my_msg="Security Breach at door.KIndly check mail for the person's pic"
	message=client.messages.create(to=my_num,from_=twil_no,body=my_msg)

