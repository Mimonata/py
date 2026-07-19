# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/18 08:19:18 by spitul            #+#    #+#              #
#    Updated: 2026/07/19 21:44:24 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

players = ["Dudi", "miki", "Mili", "Akai", "deri", "toku"]

def main():
	capitalized_names = []
	capitaled = []
	capitalized_names = [name.capitalize() for name in players]
	capitaled = [name for name in players if name == name.capitalize()]
	print("=== Game Data Alchemist ===\n")
	print(f"Initial list of players: {players}")
	print(f"New list with all names capitalized: {capitalized_names}")
	print(f"New list of capitalized names only: {capitaled}\n")

	scores = {name: random.randint(0, 1000) for name in capitalized_names}
	print("Scores dict: ", scores)
	average = sum(scores.values()) / len(scores)
	print("Score average is:", round(average, 2))
	high_score = {name: val for name, val in scores.items() if val > average}
	print("High scores", high_score)

if __name__ == "__main__":
	main()
	exit (0)
	