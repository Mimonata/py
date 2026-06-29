# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    load_image.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/20 08:46:36 by spitul            #+#    #+#              #
#    Updated: 2026/06/22 22:00:14 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
	# if not path.endswith(".jpg") and not path.endswith(".jpeg"):
	# 	raise ValueError("File not the right format")
	try:
		img = Image.open(path)
	except FileNotFoundError as e:
		print(e)
		return None
	if not img.format == "JPEG" and not img.format == "JPG":
		raise ValueError("Wrong format")
	arr = np.array(img)
	print(f"The shape of the image is: {arr.shape}")
	print(arr)
	return arr
	