# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pimp_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 07:33:09 by spitul            #+#    #+#              #
#    Updated: 2026/07/01 21:35:16 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np
# # np.uint8(255) + 1
# a = np.array([100,200,30])
# b = 255 - a
# print(a)
# print(b)

def ft_invert(array) -> np.ndarray:
	"""This function inverts the colors in an image"""
	inverted = 255 - array
	plt.imshow(inverted)
	plt.show()
	print(inverted)
	return inverted


# def ft_red(array) -> array:


# def ft_green(array) -> array:


# def ft_blue(array) -> array:


# def ft_grey(array) -> array:

