# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rotate.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 20:27:44 by spitul            #+#    #+#              #
#    Updated: 2026/06/26 22:10:15 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import sys
import numpy

sys.path.append("../ex02")
from load_image import ft_load
sys.path.append("../ex03")
from zoom import zoom

def	rotate():
	# arr = ft_load("test_img.jpg")
	zoomed = zoom()
	rows, cols = zoomed.shape
	transposed = numpy.zeros((cols, rows), dtype = zoomed.dtype)
	for y in range(rows):
		for x in range(cols):
			transposed[x][y] = zoomed[y][x]
	plt.imshow(transposed, cmap="gray")
	plt.savefig("output.jpg")
	print(f"New shape after transpose: {transposed.shape}")
	print(transposed)
	
if __name__ == "__main__":
	rotate()
