# # sorting lists

# # if we sort numbers, they will be sorted in ascending order
# my_list = [3, 6, 4, 2, 1, 5]
# my_list.sort()
# print(my_list)


# # If we sort strings, they will be sorted in alphanumeric order
# my_list = ['csbbsge', 'apple', 'banana', 'potato']
# my_list.sort()
# print(my_list)


# my_list = ['This is a long sentence', 'Word', 'z']

# # What if we want to sort by the length of the string?
# # We can use the key attribute to tell the sort function to sort using the len function.

# my_list.sort(key = len)
# print(my_list)
# # => ['z', 'Word', 'This is a long sentence']

# # If we want to sort in descending order we can pass in the reverse parameter into sort.
# my_list = ['This is a long sentence', 'Word', 'z']
# my_list.sort(key = len, reverse=True)
# print(my_list)
# # => ['This is a long sentence', 'Word', 'z']


# my_list = [('John', 2), ('Steve', 1), ('Joe', 3)]

# # We can define a function for the list to sort by the second key

# def sort_tuple(tuple_value):

#     # return the key we want to sort by
#     return tuple_value[1]

# my_list.sort(key = sort_tuple)
# print(my_list)
# # => [('Steve', 1), ('John', 2), ('Joe', 3)]

# my_list = [3, 6, 4, 2, 1, 5]
# sorted_list = sorted(my_list)
# print(my_list)
# # => [3, 6, 4, 2, 1, 5]
# print(sorted_list)
# # => [1, 2, 3, 4, 5, 6]


# my_list = ['Loquacious', 'Chatty', 'Talkative']
# sorted_list = sorted(my_list, key=len, reverse=True)
# # => ['Loquacious', 'Talkative', 'Chatty']


# my_list = [0, 1, 2, 3]
# my_list[0] = None
# print(my_list)
# # => [None, 1, 2, 3]


# my_list = [0, 1, 2, 3]
# my_list[4] = 4
# # => IndexError: list assignment index out of range


# my_list = [0, 1, 2, 3]
# my_list.append(4)
# print(my_list)
# # => [0, 1, 2, 3, 4]


# my_list = ['a', 'b', 'c', 'd', 'f']
# my_list.insert(4, 'e')
# print(my_list)
# # => ['a', 'b', 'c', 'd', 'e', 'f']
# my_list.insert(1000, 'g')
# print(my_list)
# # => ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# #Adding to lists
# my_list = [0, 1, 2, 3,]
# my_list[0] = None
# print(my_list)


# my_list = [0, 1, 2, 3]
# my_list[4] = 4
# # => IndexError: list assignment index out of range


# my_list = [0, 1, 2, 3]
# my_list.append(4)
# print(my_list)
# # => [0, 1, 2, 3, 4]


# my_list = ['a', 'b', 'c', 'd', 'f']
# my_list.insert(4, 'e')
# print(my_list)
# # => ['a', 'b', 'c', 'd', 'e', 'f']
# my_list.insert(1000, 'g')
# print(my_list)
# # => ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# # Removing from lists

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0])
# print(my_list)
# # => ['b', 'c', 'd', 'e', 'f', 'g']
# del(my_list[0:3])
# print(my_list)
# # => ['e', 'f', 'g']

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# my_list.pop()
# # => 'g'
# my_list.pop(0)
# # => 'a'
# my_list.remove('f')
# print(my_list)
# # => ['b', 'c', 'd', 'e']
# my_list.clear()
# print(my_list)
# # => []

# for n in range(4):
#     print(n)

# my_list = [0, 1, 2, 3]
# print(my_list)
# # => [0, 1, 2, 3]

# my_range = range(4)
# print(my_range)
# # => range(0, 4)

# my_string = 'Hello world!'
# for char in my_string:
#     print(char)

# # => H
# # => e
# # => l
# # => l
# # => o
# # =>
# # => w
# # => o
# # => r
# # => l
# # => d
# # => !


# my_string[0]
# # => 'H'

my_string = 'hello world!'
my_string.upper()
# => HELLO WORLD!
print(my_string.title())
# => hello world!