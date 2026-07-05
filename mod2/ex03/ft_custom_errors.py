# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 22:48:44 by spitul            #+#    #+#              #
#    Updated: 2026/07/05 22:06:17 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
	def __init__(self, message="Unknown garden error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message="Unknown plant error"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message="Unknown water error"):
		super().__init__(message)

def WaterTester(water: float) -> None:
	if (water < 0.8):
		raise WaterError("Not enough water in the tank!")

def	PlantTester(plant: str) -> None:
	if (plant != "green"):
		raise PlantError("The tomato plant is wilting")

if __name__ == "__main__":
	print("== Custom Garden Errors Demo ==")
	print("\nTesting WaterError...")
	try:
		WaterTester(0.1)
	except WaterError as e:
		print("Caught WaterError:", e)
	print("\nTesting PlantError...")
	try:
		PlantTester("yellow")
	except PlantError as e:
		print("Caught PlantError:", e)
	print("\nTesting catching all garden errors...")
	try:
		WaterTester(0.1)
	except GardenError as e:
		print("Caught GardenError:", e)
	try:
		PlantTester("yellow")
	except GardenError as e:
		print("Caught GardenError:", e)
		
	print("\nAll custom error types work correctly!")
		