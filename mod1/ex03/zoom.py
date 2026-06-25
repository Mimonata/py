# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    zoom.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/22 22:05:09 by spitul            #+#    #+#              #
#    Updated: 2026/06/25 20:24:16 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import sys
import numpy

sys.path.append("../ex02")
from load_image import ft_load

def zoom():
	arr = ft_load("test_img.jpg")
	zoomed = arr[200:600, 200:600, 0:1]
	plt.imshow(zoomed, cmap="gray")
	plt.savefig("output.jpg")
	print(f"New shape after slicing {zoomed.shape}")
	print(zoomed)
	
if __name__ == "__main__":
	zoom()
	