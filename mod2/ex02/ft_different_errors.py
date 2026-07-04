# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 22:57:21 by spitul            #+#    #+#              #
#    Updated: 2026/07/04 22:44:42 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(operation_number: int) -> None:
	if (operation_number == 1):
		operation_number / 0
	elif (operation_number == 0):
		int("abc")
	elif (operation_number == 2):
		fo = open("/non/existent/file")
	elif (operation_number == 3):
		"abc" + 2
	else:
		return

def test_error_types():
	print("=== Garden Error Types Demo ===")
	for x in range(5):
		try:
			print(f"Testing operation {x}...")
			garden_operations(x)
			print("Operation completed successfully")
		except ValueError as e:
			print("Caught ValueError:", e)
		except TypeError as e:
			print("Caught TypeError:", e)
		except ZeroDivisionError as e:
			print("Caught ZeroDivisionError:", e)
		except FileNotFoundError as e:
			print("Caught FileNotFoundError:", e)
	print("\nAll error types tested successfully!")
				
if __name__ == "__main__":
	test_error_types()
	