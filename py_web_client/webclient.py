# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    webclient.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 07:38:54 by spitul            #+#    #+#              #
#    Updated: 2026/02/12 19:12:38 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import sys
from urllib import urlparse

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

def	webclient(sys.argv) -> str:

	input = sys.argv.split(" ")
	if (len(input) == 3):
		port = atoi(input[2])
	elif (len(input) == 2):
		port = 80
	else:
		print("Wrong input")
	url = input[1]
	
	if "://" not in url
		url = "http://" + url
	parsed = urlparse(url)
	response = send_http_request(parsed, port)
	print(response)
