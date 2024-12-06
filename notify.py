#!/bin/python3

import os
import sys
from json import dumps
from httplib2 import Http

def main():
	"""Send message via Hangouts Chat incoming webhook"""
	msg = ' '.join(sys.argv[1:])

	if len(msg) == 0:
		print('No message to send', file=sys.stderr)
		return 1

	url = os.environ.get('NOTIFIER_CHAT_URL')

	if url == None:
		print("Unable to locate chat url", file=sys.stderr)
		return 2


	message = {'text' : msg}

	message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

	http_obj = Http()

	response = http_obj.request(
		uri=url,
		method='POST',
		headers=message_headers,
		body=dumps(message),
	)

	#print(response)

if __name__ == '__main__':
	main()
