# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/09 22:44:29 by spitul            #+#    #+#              #
#    Updated: 2026/07/10 22:51:15 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def gen_player_achievement() -> set:
	all_achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
		'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',
		'Untouchable', 'Sharp Mind', 'Boss Slayer']
	count = random.randint(3, 13)
	achievements = random.sample(all_achievements, count)
	return set(achievements)

def print_achievemts(name: str, player: set, msg: str) -> None:
	print(f"{msg} {name}: {player}")

def main():
	player_one = gen_player_achievement()
	player_two = gen_player_achievement()
	player_three = gen_player_achievement()
	player_four = gen_player_achievement()
	all = {"Hen":player_one, "Mim":player_two, "Akira":player_three, "Sony":player_four}
	for player, name in all.items():
		print_achievemts(name, player, "Player: ")
	all_ach = player_four.union(player_one, player_three, player_two)
	print(f"\nAll distinct achievements: {all_ach}\n")
	common = player_four & player_one & player_three & player_two
	print(f"Common achievements: {common}\n")
	
	for player, name in all:
		print_achievemts(name, player.difference(all_ach - player), f"Only {name} has:")
	
	
	Track unique achievements among all the players
• Find achievements shared by all players
• For each player, spot the achievements no one else has
• For each player, list the missing achievements to have them all