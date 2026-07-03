# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/03 07:11:57 by spitul            #+#    #+#              #
#    Updated: 2026/07/03 07:19:22 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import traceback

#try:
#	raise ValueError("test")
# except ValueError as e:
# 	traceback.print_tb(e.__traceback__)
# 	print(type(e))
a = [1,2,3]
print(a[10])