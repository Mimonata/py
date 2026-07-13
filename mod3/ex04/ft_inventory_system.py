# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/11 08:22:08 by spitul            #+#    #+#              #
#    Updated: 2026/07/13 21:44:38 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parse_inventory() -> None:
	if len(sys.argv) == 1:
		print("No inventory provided")
		return
	inventory = {}
	for x in sys.argv[1:]:
		parts = x.split(":")
		if len(parts) != 2:
			print(f"Error - invalid parameter '{x}'")
		try:
			amount = int(parts[1])
			if amount < 0:
				raise Exception("Quantity cannot be negative")
		except Exception as e:
			print(f"Quantity error for '{parts[0]}': {e}")
		if parts[0] in inventory:
			print(f"Redundant item '{parts[0]}' - discarding")
		inventory[parts[0]] = amount
	
	print(f"Got inventory: {inventory}")
	print(f"Item list: {list(inventory.keys())}")
	summe = sum(inventory.values())
	print(f"Total quantity of the {len(inventory)} items is: {summe}")
	for item, qty in inventory.items():
		percentage = round(qty / summe * 100, 2)
		print(f"Item {inventory[item]} represents {percentage}%")
	min = float('inf')
	max = 0
	for item, qty in inventory.items():
		if qty < min:
			min_item = item
		elif qty > max:
			max_item = item
	print(f"Item most abundant: {max} with quantity {max_item}")
	print(f"Item least abundant: {min} with quantity {min_item}")
	dict.update({"new_inventory_bucket": 10})
	print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
	parse_inventory()
	exit(0)
	