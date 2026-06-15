# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/13 19:20:27 by spitul            #+#    #+#              #
#    Updated: 2026/06/15 21:30:04 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from time import time

from tqdm import tqdm
from typing import Iterable

def ft_tqdm(lst: range) -> None:
	width = os.get_terminal_size().columns
	length = len(lst)
	last_print = time()
	for i, item in enumerate(lst):
		percent = (100 * (i + 1)) / length
		prefix = f"{int(percent)}%|["
		sufix = f"]| {i + 1}/{length}"
		bar_width = width - len(prefix) - len(sufix) - 1
		if (time() - last_print >= 0.1 or i == length - 1):
			print(f'\r{prefix}{int(percent * (bar_width / 100)) * "="}>{sufix}', end='', flush=True)
			last_print = time()
		yield item
	