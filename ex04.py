# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 21:10:39 by spitul            #+#    #+#              #
#    Updated: 2026/05/21 07:17:40 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def whatis():
	assert len(sys.argv) <= 2, "more than one argument provided"
	if len(sys.argv) == 2:
		arg = sys.argv[1]
		assert arg.lstrip('+-').isdigit(), "argument is not an integer"
		if int(arg) % 2 == 1:
			print("I'm odd")
		else:
			print("I'm even")

	# side quest
	txt = "The best things in life are free!"
	print("free" in txt)

if __name__ == "__main__":

	try:
		whatis()
	except AssertionError as e:
		print(e)
		sys.exit(1)
