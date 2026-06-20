# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 21:40:31 by spitul            #+#    #+#              #
#    Updated: 2026/06/20 08:37:22 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from array2D import slice_me

family = [[1.80, 78.4],
		[2.15, 102.7],
		[2.10],
		[1.88, 75.2]]
fam = [[]]
try: 
	print(slice_me(family, 0, 2))
	print(slice_me(family, 1, -2))
except Exception as e:
	print(e)
