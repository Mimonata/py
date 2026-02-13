# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mario.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/12 19:13:20 by spitul            #+#    #+#              #
#    Updated: 2026/02/12 20:46:00 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

size = int(input("Height: "))
array = ""
k = 1
for i in range(size):
	for j in range(size):
		if size - k <= j:
			print(f"#", end="")
		else:
			print(" ", end="")
	k += 1
	print("")
print("")

for i in range(size + 1):
	print(" " * (size - i) + "#" * i + " " + "#" * i + " " * (size - i))
		