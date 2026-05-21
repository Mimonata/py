# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester_ex03.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 20:16:05 by spitul            #+#    #+#              #
#    Updated: 2026/05/20 20:47:51 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex03 import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
