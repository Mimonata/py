# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 21:28:14 by spitul            #+#    #+#              #
#    Updated: 2026/06/20 08:41:43 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
		raise TypeError("Input must be a 2D list of lists")
	try:
		arr = np.array(family)
	except ValueError:
		raise ValueError("Input rows not homogenous")
	print(f"My shape is : {arr.shape}")
	slice = arr[start:end]
	print(f"My new shape is : {slice.shape}")
	return slice.tolist()
