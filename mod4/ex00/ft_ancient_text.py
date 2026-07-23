# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/20 20:53:31 by spitul            #+#    #+#              #
#    Updated: 2026/07/23 20:13:57 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
		exit(0)
	try:
		print("=== Cyber Archives Recovery ===")
		print(f"Accessing file '{sys.argv[1]}'")
		file = open(sys.argv[1])
		print("---\n")
		print(file.read())
		print("\n---")
		file.close()
		print(f"File '{sys.argv[1]}' closed.")
	except Exception as e:
		print(f"Error opening '{sys.argv[1]}':", e)
		
if __name__ == "__main__":
	main()
	exit(0)
	