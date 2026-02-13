# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    webclient.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 07:38:54 by spitul            #+#    #+#              #
#    Updated: 2026/02/13 08:48:20 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import sys
from urllib.parse import urlparse

# python webclient.py example.com

def	receive_response(sock):
	
	response = b""
	while True:
		data = sock.recv(4096)
		if not data:
			break
		response += data
	return response.decode()

def	send_http_request(url, port) -> str:

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(url.hostname, port)
	request = f"GET {url.path} HTTP/1.1\r\nHost: {url.hostname}\r\nConnection: close\r\n\r\n"
	sock.sendall(request.encode())
	response = receive_response(sock)
	sock.close()
	return response

def	webclient() -> str:

	if (len(sys.argv) == 3):
		port = int(sys.argv[2])
	elif (len(sys.argv) == 2):
		port = 80
	else:
		print("Wrong input")
	url = sys.argv[1]
	
	if "://" not in url:
		url = "http://" + url
	parsed = urlparse(url)
	response = send_http_request(parsed, port)
	print(response)
