# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/14 18:27:02 by spitul            #+#    #+#              #
#    Updated: 2026/07/18 08:17:11 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

import typing

players = ["1", "2", "3", "4", "5", "6", "7"]
actions = ["read", "draw", "research", "run", "eat", "swim", "sleep"]

def gen_event() -> typing.Generator:
	while True:
		yield(random.choice(players), random.choice(actions))

def consume_event(ev_list: list) -> typing.Generator:
	while ev_list:
		yield (ev_list.pop(random.randint(0, len(ev_list) - 1)))

def main():
	gen = gen_event()
	for x in range(1000):
		event = next(gen)
		print(f"Event {x}: Player {event[0]} did action {event[1]}")
	
	ev_list = []
	for x in range(10):
		ev_list.append(next(gen))
	print(f"Built list of ten events: {ev_list}")
	
	consumed = consume_event(ev_list)
	for event in consumed:
		event = next(consumed)
		print(f"Got event from list: {event}")
		print(f"Remains in list {ev_list}")

if __name__ == "__main__":
	main()
	exit (0)