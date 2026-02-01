# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    webclient.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 07:38:54 by spitul            #+#    #+#              #
#    Updated: 2026/02/01 20:27:36 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import socket
import sys

# python webclient.py example.com

def	webclient(sys.argv) -> str
	input = sys.argv.split(" ")
	if (len(input) == 3)
		port = atoi(input[2])
	elif (len(input) == 2)
		port = 80
	else
		print("Wrong input")
	url = input[1]
	
	if "://" not in url
		url = "http://" + url
	parts = url.split("://")[1].split("/")
	
	
