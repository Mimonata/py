# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    give_bmi.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 06:19:07 by spitul            #+#    #+#              #
#    Updated: 2026/06/19 21:32:20 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	assert len(height) == len(weight), "Weight and height list have different lengths"
	for x in height:
		assert isinstance(x, (int, float)), "Wrong type in Height"
	for x in weight:
		assert isinstance(x,(int, float)), "Wrong type in Weight"
	height = np.array(height)
	weight = np.array(weight)
	bmi = weight / height ** 2
	return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	res = []
	for x in bmi:
		assert isinstance(x, (int, float)), "Wrong type in Bmi"
		if x > limit:
			res.append(True)
		else:
			res.append(False)
	return res
	
	# return (np.array(bmi) > limit).tolist()
	