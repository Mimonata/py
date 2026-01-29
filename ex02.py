# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 20:48:20 by spitul            #+#    #+#              #
#    Updated: 2026/01/29 06:53:22 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Any

def all_thing_is_obj(object: Any) -> int:
	if (type(object) == list):
		print(f"List : {type(object)}")
	elif (type(object) == tuple):
		print(f"Tuple : {type(object)}")
	elif (type(object) == set):
		print(f"Set : {type(object)}")
	elif (type(object) == dict):
		print(f"Dict : {type(object)}")
	elif (type(object) == str):
		print(f"{object} is in the kitchen : {type(object)}")
	else:
		print("Type not found")
	return 42
	