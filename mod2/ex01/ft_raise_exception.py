# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 22:45:11 by spitul            #+#    #+#              #
#    Updated: 2026/07/03 23:01:13 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(data: str) -> int:
	rez = int(data)
	if (rez < 0):
		raise ValueError(f"{data}°C is too cold for plants (min 0°C)")
	elif (rez > 40):
		raise ValueError(f"{data}°C is too hot for plants (max 40°C)")
	print(f"Temperature is now {data}°C\n")
	return rez

def test_temperature() -> None:
	try:
		print("Input data is '25'")
		input_temperature("25")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")
	try:
		print("Input data is 'abc'")
		input_temperature("abc")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")
	try:
		print("Input data is '100'")
		input_temperature("100")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")
	try:
		print("Input data is '-50'")
		input_temperature("-50")
	except Exception as e:
		print(f"Caught input_temperature error: {e}\n")
	
if __name__ == "__main__":
	print("\n=== Garden Temperature Checker ===\n")
	test_temperature()
	print("All tests completed - program didn't crash!")
		