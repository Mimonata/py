# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 20:46:38 by spitul            #+#    #+#              #
#    Updated: 2026/07/06 20:56:37 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# > python3 ft_command_quest.py
# === Command Quest ===
# Program name: ft_command_quest.py
# No arguments provided!
# Total arguments: 1
# $> python3 ft_command_quest.py hello world 42
# === Command Quest ===
# Program name: ft_command_quest.py
# Arguments received: 3
# Argument 1: hello
# Argument 2: world
# Argument 3: 42
# Total arguments: 4


if __name__ == "__main__":
	print("=== Command Quest ===")
	print("Program name:", sys.argv[0])
	len = len(sys.argv)
	if len == 1:
		print("No arguments provided!")
	else:
		for i, val in enumerate(sys.argv[1:], start=1):
			print(f"Argument {i}: {val}")
	print("Total arguments:", len)
