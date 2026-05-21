# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 19:18:24 by spitul            #+#    #+#              #
#    Updated: 2026/05/21 07:19:31 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Any


def NULL_not_found(object: Any) -> int:
	if (object is None):
		print (f"Nothing: {object} {type(object)}")
		return 0
	elif (type(object) == float and object != object):
		print(f"Cheese: {object} {type(object)}")
		return 0
	elif (type(object) == int and object == 0):
		print(f"Zero: {object} {type(object)}")
		return 0
	elif (type(object) is str and object == ""):
		print(f"Empty: {type(object)}")
		return 0
	elif (type(object) is bool and object == 0):
		print(f"Fake: {object} {type(object)}")
		return 0
	else:
		print("Type not found")
		return 1
