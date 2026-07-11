# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/11 08:22:08 by spitul            #+#    #+#              #
#    Updated: 2026/07/11 08:30:27 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parse_inventory() -> None:
	if len(sys.argv == 1):
		print("No inventory provided")
		return
	inventory = {}
	for x in sys.argv[1:]:
			
