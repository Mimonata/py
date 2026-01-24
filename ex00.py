# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: spitul <spitul@student.42berlin.de >       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/24 13:37:06 by spitul            #+#    #+#              #
#    Updated: 2026/01/24 13:55:37 by spitul           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	test():
	ft_list = ["Hello", "tata!"]
	ft_tuple = ("Hello", "toto!")
	ft_set = {"Hello", "tutu!"}
	ft_dict = {"Hello" : "titi!"}
	
	ft_list[1] = "World"
	ft_tuple = ("Hello", "Germany")
	ft_set.remove("tutu!")
	ft_set.add("Berlin")
	ft_dict["Hello"] = "42Berlin"

	print(ft_list)
	print(ft_tuple)
	print(ft_set)
	print(ft_dict)
	
test()
