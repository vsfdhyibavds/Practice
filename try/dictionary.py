# dog = "cuddly"

# dict_map = {
#     "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")

# setting data

# my_dict = {
#     "key_one": "value one",
#     "key_two": "value two",
# }

# # update an existing key-value pair:
# my_dict["key_one"] = "I've changed!"

# # set a new key-value pair:
# my_dict["key_three"] = "value three"

# print(my_dict)
# # prints { "key_one": "I've changed!", "key_two": "value two", "key_three": "value three"}

# my_dict = {
#     "key_one": "value one",
#     "key_two": "value two",
# }

# # update multiple fields:
# my_dict.update({"key_one": "new value one", "key_two": "new value two"})

# # add multiple fields:
# my_dict.update({"key_three": "value three", "key_four": "value four"})

# # add and update fields simultaneously:
# my_dict.update({"key_three": "new value three", "key_four": "new value four", "key_five": "value five"})

# print(my_dict)
# # prints {'key_one': 'new value one', 'key_two': 'new value two', 'key_three': 'new value three', 'key_four': 'new value four', 'key_five': 'value five'}

# my_dict = {
#     "key_one": "value one"
# }

# # passing in an array of arrays
# my_dict.update([["key_one", "new value one"], ["key_two", "value two"]])

# # passing in an array of tuples
# my_dict.update([("key_two", "new value two"), ("key_three", "value three")])

# # passing in a tuple of arrays
# my_dict.update((["key_three", "new value three"], ["key_four", "value four"]))

# # passing in a tuple of tuples
# my_dict.update((("key_four", "new value four"), ("key_five", "value five")))

# # using assignment operation
# my_dict.update(key_five="new value five", key_six="value six")

# print(my_dict)
# # prints {'key_one': 'new value one', 'key_two': 'new value two', 'key_three': 'new value three', 'key_four': 'new value four', 'key_five': 'new value five', 'key_six': 'value six'}


# Iterating over Dictionaries

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

[key for key in my_dict]
# ['a', 'b', 'c', 'd']
[my_dict[key] for key in my_dict]
# [1, 2, 3, 4]

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

[item for item in my_dict.items()]
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
[key for key, value in my_dict.items()]
# ['a', 'b', 'c', 'd']
[value for key, value in my_dict.items()]
# [1, 2, 3, 4]