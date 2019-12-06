"""
This is a python implementation of linear search algorithm

python
"""
import random


def linear_search(array,key):
    for value in array:
        if key ==value:
            return True


list = [random.randint(0, 100) for x in range(1, 11)]
key = random.randrange(1,100)
print('Random list of integers {}'.format(list))
print('key to be searched is {}'.format(key))

if linear_search(list,key):
    print('{} is found in the list {}'.format(key,list))
else:
    print('{} is not found in the list{}'.format(key,list))