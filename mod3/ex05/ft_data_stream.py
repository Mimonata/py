# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/14 18:27:02 by spitul            #+#    #+#              #
#    Updated: 2026/07/17 20:37:43 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

players = ["1", "2", "3", "4", "5", "6", "7"]
actions = ["read", "draw", "research", "run", "eat", "swim", "sleep"]

def gen_event():
	while True:
		yield(random.choice(players), random.choice(actions))

def main():
	gen = gen_event()
	for x in range(1000):
		event = next(gen)
		print(f"Event {x}: Player {event[0]} did action {event[1]}")
		