# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 22:37:59 by spitul            #+#    #+#              #
#    Updated: 2026/07/09 22:36:07 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ORANGE     = "\033[38;5;208m"
SOFT_BLUE  = "\033[38;5;67m"
MUTED_GREEN = "\033[38;5;71m"
DUSTY_PINK = "\033[38;5;181m"
WARM_GREY  = "\033[38;5;245m"
RESET      = "\033[0m"

import sys

def score_parser() -> None:
	len_argv = len(sys.argv)
	if (len_argv == 1):
		print(f"{MUTED_GREEN}No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...{RESET}")
		return None
	sum = 0
	lst = []
	for x in sys.argv[1:]:
		try:
			lst.append(int(x))
		except Exception:
			print(f"{DUSTY_PINK}Invalid parameter: '{x}'{RESET}")
	for x in lst:
		sum += x
	print(f"Scores processed: {lst}")
	print(f"Total players: {len(lst)}")
	print(f"Total score: {sum}")
	print(f"Average score: {sum/(len(lst) - 1)}")
	print(f"High score: {max(lst)}")
	print(f"Low score: {min(lst)}")
	print(f"Score range: {max(lst) - min(lst)}")

if __name__ == "__main__":
	print(f"{ORANGE}=== Player Score Analytics ==={RESET}")
	score_parser()	
	