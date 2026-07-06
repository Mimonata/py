# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 19:58:58 by spitul            #+#    #+#              #
#    Updated: 2026/07/06 20:34:41 by spitul           ###   ########.fr        #
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

def water_plant(plant_name: str) -> None:
	temp = plant_name.capitalize()
	if (temp == plant_name):
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")
	
def test_watering_system() -> None:
	print("=== Garden Watering System ===\n")
	print("Testing with valid plants ...")
	print("Opening watering system")
	try:
		water_plant("Cactus")
		water_plant("Kranzschlinge")
		water_plant("Olivarda")
	except PlantError as e:
		print("Caught PlantError:", e)
		return(print("... ending tests and returning to main"))
	finally:
		print("Closing Watering system\n")
	
	print("Testing with invalid plants ...")
	print("Opening watering system")
	try:
		water_plant("Cactus")
		water_plant("kranzschlinge")
		water_plant("Olivarda")
	except PlantError as e:
		print("Caught PlantError:", e)
		return(print("... ending tests and returning to main"))
	finally:
		print("Closing Watering system\n")
	
if __name__ == "__main__":
	test_watering_system()
	print("Cleanup always happens even with errors!")
	exit(0)
	