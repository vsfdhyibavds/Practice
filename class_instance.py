# Remember that Python requires some indented code in each code block.
# Instead of empty blocks, we use the "pass" keyword to do nothing.

class Dog:
    pass

fido = Dog()
fido
# <__main__.Dog object at 0x1049a87f0>

class Dog:
    pass

fido = Dog()
fido
# <__main__.Dog object at 0x1049a87f0>

snoopy = Dog()
snoopy
# <__main__.Dog object at 0x104971d90>

class Dog:
    pass

fido = Dog()
fido
# <__main__.Dog object at 0x1049a87f0>

snoopy = Dog()
snoopy
# <__main__.Dog object at 0x104971d90>

lassie = Dog()
lassie
# <__main__.Dog object at 0x10498c040>

class Dog:
    pass

fido = Dog()
fido
# <__main__.Dog object at 0x1049a87f0>

snoopy = Dog()
snoopy
# <__main__.Dog object at 0x104971d90>

snoopy == fido
# False