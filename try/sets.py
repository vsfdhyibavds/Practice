my_set = set([1, 2, 3])
my_set = {1, 2, 3}

my_list = [1, 2, 1, 3, 2]
set(my_list)
# {1, 2, 3}

my_string = "the big red cat ate the fat rat"
set(my_string)
# {'g', 'h', 'b', 'r', 'e', 'd', 'f', 'c', 't', 'a', 'i', ' '}

set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# True

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 & set_2
# 3

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 - set_2
# {1, 2}
set_2 - set_1
# {4, 5}

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 &= set_2
# {3}
set_2 -= set_1
# {4, 5}

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
# {'g', 'p', 'b', 'l', 'r', 'd', 'm', 'q', 'c', 't', 's', 'n'}