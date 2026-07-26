# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stream_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/25 21:27:54 by spitul            #+#    #+#              #
#    Updated: 2026/07/26 09:10:01 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def extract_file() -> str:
	if len(sys.argv) != 2:
		sys.stderr.write("[STDERR] Usage: ft_ancient_text.py <file>\n")
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
		sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
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
	sys.stdout.write("Enter new file name (or empty): ")
	sys.stdout.flush()
	outfile = sys.stdin.readline().strip()
	if outfile == "":
		print("Not saving data.")
	else:
		try: 
			file = open(outfile, "w")
			print(f"Saving data to '{outfile}'.")
			file.write(text)
			print(f"Data saved in file '{outfile}'.")
			file.close()
		except Exception as e:
			sys.stderr.write(f"[STDERR] Error opening file '{outfile}': {e}\n")
			sys.stdout.write("Data not saved.")
	
if __name__ == "__main__":
	text = extract_file()
	transform_data(text)
	exit(0)
	
