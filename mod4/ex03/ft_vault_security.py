# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/26 09:14:29 by spitul            #+#    #+#              #
#    Updated: 2026/07/27 20:48:48 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Tuple

def secure_archive(filename: str, action="read", content=None) -> Tuple[bool, str]:
	try:
		if action == "read":
			with open(filename, "r") as file:
				text = file.read()
				return (True, text)
		if action == "write":
			with open(filename, "w") as file:
				file.write(content)
				return (True, 'Content successfully written to file')
	except Exception as e:
		return (False, str(e))

def main() -> int:
	print("=== Cyber Archives Security ===\n")
	print(f"Using 'secure_archive' to read from a nonexistent file:")
	print(secure_archive("nonexist", "read"))
	print(f"\nUsing 'secure_archive' to read from an inaccesible file:")
	print(secure_archive("inaccessible", "read"))
	print(f"\nUsing 'secure_archive' to read from a regular file:")
	tup = secure_archive("test.txt", "read")
	print(tup)
	print(f"\nUsing 'secure_archive' to write previous content to a new file:")
	print(secure_archive("out", "write", tup[1]))

if __name__ == "__main__":
	main()
	exit(0)
