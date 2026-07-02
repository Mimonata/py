# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pimp_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/29 07:33:09 by spitul            #+#    #+#              #
#    Updated: 2026/07/02 21:33:05 by spitul           ###   ########.fr        #
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

def ft_green(array) -> np.ndarray:
	"""Function ft_green renders a picture in its green tones"""
	greened = array.copy()
	greened[:, :, 0] = array[:, :, 0] - array[:, :, 0]
	greened[:, :, 2] = array[:, :, 2] - array[:, :, 2]
	plt.imshow(greened)
	plt.show()
	print(greened)
	return greened


def ft_blue(array) -> np.ndarray:
	"""Function ft_blue for displaying the blue tones of an image"""
	blued = array.copy()
	blued[:, :, 0] = 0
	blued[:, :, 1] = 0
	plt.imshow(blued)
	plt.show()
	print(blued)
	return blued


def ft_grey(array) -> np.ndarray:
	"""ft_gray for black and white image display"""
	greyed = array.copy()
	temp = greyed.mean(axis=2, keepdims=True)
	greyed[:] = temp
	plt.imshow(greyed)
	plt.show()
	print(greyed)
	return greyed

if __name__ == "__main__":
	array = ft_load("test_img.jpg")
	ft_invert(array)
	ft_red(array)
	ft_green(array)
	ft_blue(array)
	ft_grey(array)
