# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/16 21:37:35 by spitul            #+#    #+#              #
#    Updated: 2026/06/16 21:37:37 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # should print 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # should print 0
