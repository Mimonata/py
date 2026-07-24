# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_archive_creation.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/23 20:16:19 by spitul            #+#    #+#              #
#    Updated: 2026/07/24 22:27:20 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def extract_file() -> str:
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
		exit(0)
	text = ""
	try:
		print("=== Cyber Archives Recovery & Preservation ===")
		print(f"Accessing file '{sys.argv[1]}'")
		file = open(sys.argv[1])
		print("---\n")
		text = file.read()
		print(text)
		print("\n---")
		file.close()
		print(f"File '{sys.argv[1]}' closed.")
	except Exception as e:
		print(f"Error opening '{sys.argv[1]}':", e)
	return text

def transform_data(text: str) -> None:
	print("\nTransform data:")
	print("---\n")
	new_lines = []
	lines = text.split("\n")
	for line in lines:
		extended = line + "#"
		new_lines.append(extended)
	text = '\n'.join(new_lines)
	print(text)
	print("\n---")
	outfile = input("Enter new file name (or empty): ")
	if outfile == "":
		print("Not saving data.")
	else:
		file = open(outfile, "w")
		print(f"Saving data to '{outfile}'.")
		file.write(text)
		print(f"Data saved in file '{outfile}'.")
		file.close()
	
if __name__ == "__main__":
	text = extract_file()
	transform_data(text)
	exit(0)
	