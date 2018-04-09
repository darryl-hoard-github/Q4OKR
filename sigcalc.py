from hashlib import sha1 
import hmac
import time 

try:
    # Python 3
    from http.server import HTTPServer, SimpleHTTPRequestHandler, test as test_orig
    import sys
    def test (*args):
        test_orig(*args, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
except ImportError: # Python 2
    from BaseHTTPServer import HTTPServer, test
    from SimpleHTTPServer import SimpleHTTPRequestHandler

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer)

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

	return hashed 
