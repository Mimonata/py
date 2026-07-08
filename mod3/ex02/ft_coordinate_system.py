# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/07 20:18:46 by spitul            #+#    #+#              #
#    Updated: 2026/07/08 22:34:17 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def get_player_pos():
	while True:
		str = input("Enter new coordinates as floats in format 'x,y,z': ")
		coord = str.split(",")
		if (len(coord) != 3):
			print("Invalid syntax")
			continue
		try:
			x = float(coord[0])
			y = float(coord[1])
			z = float(coord[2])
			return (x, y, z)
		except ValueError as e:
			print("Error on parameter:", e)
		

def main():
	print("=== Game Coordinate System ===")
	print("\nGet a first set of coordinates")
	
	coord1 = get_player_pos()
	print(f"Got a first tuple({coord1[0]}, {coord1[1]}, {coord1[2]})")
	print(f"It includes X = {coord1[0]}, Y = {coord1[1]}, Z = {coord1[2]}")
	distance = math.sqrt(coord1[0]**2 + coord1[1]**2 + coord1[2]**2)
	print("Distance to center: ", round(distance, 4))
	print("\nGet a second set of coordinates")
	coord2 = get_player_pos()
	distance = math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)
	print(f"Distance between the 2 sets of coordinates:", round(distance, 4))

if __name__ == "__main__":
	main()
	