from hashlib import sha1 
import hmac
import time 

def sign_request(nonce):
	api_id = "31d4d730-1aad-0136-9a37-0abfe2d6609e"
	time_stamp = str(time.time())
	nonce = nonce
	data = ""
	secret = "zq9EcsMxT2Y4tQwU9hQVJ3GIkNuAUnaF1XQWcJcFY"
	secret = secret.encode('utf-8')


	message = api_id+time_stamp+nonce+data
	message = message.encode('utf-8')

	hashed = hmac.new(secret, message, sha1).hexdigest()

	print(hashed)
	print(nonce)
	print(time_stamp)
