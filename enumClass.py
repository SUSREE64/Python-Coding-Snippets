"""
1. The enum is created once and values can not be added 
programatically after its creation
2. 

"""

from enum import Enum

class Animal (Enum):
	Lion = 100
	Zebra = 200
	Frog = 300
	Elephant = 400

# iterating through the Enum class
for anim in Animal:
	print(anim.name, end = "   ")
	print(anim.value)
# Accessing a memeber from enum

print("The value of the Lion is", end =" ")
print(anim.Lion.value)
