# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pimp_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 07:33:09 by spitul            #+#    #+#              #
#    Updated: 2026/07/02 07:50:41 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load
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


def ft_red(array) -> np.ndarray:
	"""The ft_red function displays and returns the red channel of the image"""
	reddend = array * [1, 0, 0]
	plt.imshow(reddend)
	plt.show()
	print(reddend)
	return reddend

# def ft_green(array) -> array:


# def ft_blue(array) -> array:


# def ft_grey(array) -> array:

if __name__ == "__main__":
	array = ft_load("test_img.jpg")
	ft_invert(array)
	ft_red(array)
