# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/09 22:44:29 by spitul            #+#    #+#              #
#    Updated: 2026/07/11 08:16:03 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

RST  = "\033[0m"
ORG  = "\033[38;5;214m"   # warm orange
LLA  = "\033[38;5;141m"   # soft lila/purple
YLW  = "\033[38;5;185m"   # dusty yellow
GRN  = "\033[38;5;107m"   # muted olive green
KHK  = "\033[38;5;143m"   # khaki
SHD  = "\033[38;5;136m"   # shadowy amber

import random

def gen_player_achievement(all_achievements: list) -> set:
	
	count = random.randint(3, 13)
	achievements = random.sample(all_achievements, count)
	return set(achievements)

def print_achievemts(player: set, msg: str, clr_code: str = None) -> None:
	print(f"{clr_code}{msg}{RST} {player}")

def main():
	print(f"\n{ORG}=== Achievement Tracker System ===\n{RST}")
	all_achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
		'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',
		'Untouchable', 'Sharp Mind', 'Boss Slayer']
	player_one = gen_player_achievement(all_achievements)
	player_two = gen_player_achievement(all_achievements)
	player_three = gen_player_achievement(all_achievements)
	player_four = gen_player_achievement(all_achievements)
	all = {"Hen":player_one, "Mim":player_two, "Akira":player_three, "Sony":player_four}
	for name, player in all.items():
		print_achievemts(player, f"Player {name}: ", GRN)
	all_ach = player_four.union(player_one, player_three, player_two)
	print(f"\n{KHK}All distinct achievements:{RST} {all_ach}\n")
	common = player_four & player_one & player_three & player_two
	print(f"{LLA}Common achievements:{RST} {common}\n")
	
	for name, player in all.items():
		others = set()
		for other_n, other_p in all.items():
			if other_n != name:
				others = others | other_p
		print_achievemts(player.difference(others), f"Only {name} has:", YLW)
	
	print()
	
	all_set = set(all_achievements)
	for name, player in all.items():
		print_achievemts(all_set.difference(player), f"{name} is missing: ", SHD)
	return 0

if __name__ == "__main__":
	main()
	