# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/01 20:21:01 by spitul            #+#    #+#              #
#    Updated: 2026/06/03 22:10:48 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_filter(func, iterable):
	if func is None:
		return [x for x in iterable if x]
	new = [x for x in iterable if func(x)]
	return new

def main():
	assert len(sys.argv) == 3, "wrong number of arguments"
	words = sys.argv[1].split()
	try:
		assert all(word.isalpha() for word in words)
		n = int(sys.argv[2])
	except:
		raise AssertionError("bad arguments")
	print(ft_filter(lambda x: len(x) > n, words))

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(e)
		sys.exit(1)
	
# 	print(filter.__doc__)
