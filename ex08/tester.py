# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/15 21:01:04 by spitul            #+#    #+#              #
#    Updated: 2026/06/15 21:18:21 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from tqdm import tqdm
from loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.010)
print()
for elem in tqdm(range(333)):
    sleep(0.010)
print()
