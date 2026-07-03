# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 07:11:57 by spitul            #+#    #+#              #
#    Updated: 2026/07/03 22:43:52 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import traceback

#try:
#	raise ValueError("test")
# except ValueError as e:
# 	traceback.print_tb(e.__traceback__)
# 	print(type(e))
# a = [1,2,3]
# print(a[10])

def input_temperature(data: str) -> int:
	rez = int(data)
	print(f"Temperature is now {data}°\n")
	return rez

def test_temperature() -> None:
	try:
		print("Input data is '25'")
		input_temperature("25")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")
	try:
		print("Input data is 'abc'")
		input_temperature("abc")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")
	
if __name__ == "__main__":
	print("\n=== Garden Temperature ===\n")
	test_temperature()
		
		