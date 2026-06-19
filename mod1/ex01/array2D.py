# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    array2D.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 21:28:14 by spitul            #+#    #+#              #
#    Updated: 2026/06/19 21:51:09 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	arr = np.array(family)
	print(f"My shape is : {arr.shape}")
	slice = arr[start:end]
	print(f"My new shape is : {slice.shape}")
	return slice.tolist()
