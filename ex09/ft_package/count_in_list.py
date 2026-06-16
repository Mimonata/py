# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_in_list.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/16 20:59:42 by spitul            #+#    #+#              #
#    Updated: 2026/06/16 21:02:24 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_in_list(lst: list, var: str) -> int:
	counter = 0
	for x in lst:
		if x == var:
			counter += 1
	return counter
