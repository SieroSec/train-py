#!/usr/bin/env python3
import re



##########################
# LIST:
##########################
# my_list = [1, "Hello", 3.4]
# # Nested List
# n_list = ["Happy", [2, 0, 1, 5]]

# # Nested indexing
# print(n_list[0][1])

# LIST METHODS:
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of the number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

##########################
# TUPLE: https://www.programiz.com/python-programming/tuple
##########################
# A tuple in Python is similar to a list. 
# The difference between the two is that we cannot change the elements of a tuple
# once it is assigned whereas we can change the elements of a list.

# my_tuple = (1, 2, 3)
# print(my_tuple)

# # tuple with mixed datatypes
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# # nested tuple
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)


##########################
# SET:
##########################

# A set is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# # set cannot have duplicates
# # Output: {1, 2, 3, 4}
# my_set = {1, 2, 3, 4, 3, 2}
# print(my_set)

# # we can make set from a list
# # Output: {1, 2, 3}
# my_set = set([1, 2, 3, 2])
# print(my_set)

# # set cannot have mutable items
# # here [3, 4] is a mutable list
# # this will cause an error.

# my_set = {1, 2, [3, 4]}

# add()	Adds an element to the set
# clear()	Removes all elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raises a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Returns the union of sets in a new set
# update()	Updates the set with the union of itself and others

# Built-in Functions with Set
# Function	Description
# all()	Returns True if all elements of the set are true (or if the set is empty).
# any()	Returns True if any element of the set is true. If the set is empty, returns False.
# enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# len()	Returns the length (the number of items) in the set.
# max()	Returns the largest item in the set.
# min()	Returns the smallest item in the set.
# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
# sum()	Returns the sum of all elements in the set.

##########################
# DICTIONARY:
##########################

# Python dictionary is an unordered collection of items.
# Each item of a dictionary has a key/value pair.

# Dictionaries are optimized to retrieve values when the key is known.

# # empty dictionary
# my_dict = {}

# # dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}

# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}

# # using dict()
# my_dict = dict({1:'apple', 2:'ball'})

# # from sequence having each item as a pair
# my_dict = dict([(1,'apple'), (2,'ball')])

# # Changing and adding Dictionary Elements
# my_dict = {'name': 'Jack', 'age': 26}

# # update value
# my_dict['age'] = 27

# #Output: {'age': 27, 'name': 'Jack'}
# print(my_dict)

# # add item
# my_dict['address'] = 'Downtown'

# # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
# print(my_dict)

# Python Dictionary Methods

# Method	Description
# clear()	Removes all items from the dictionary.
# copy()	Returns a shallow copy of the dictionary.
# fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Returns the value of the key. If the key does not exist, returns d (defaults to None).
# items()	Return a new object of the dictionary's items in (key, value) format.
# keys()	Returns a new object of the dictionary's keys.
# pop(key[,d])	Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
# popitem()	Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
# update([other])	Updates the dictionary with the key/value pairs from other, overwriting existing keys.
# values()	Returns a new object of the dictionary's values

# Dictionary Built-in Functions

# Function	Description
# all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# cmp()	Compares items of two dictionaries. (Not available in Python 3)
# sorted()	Return a new sorted list of keys in the dictionary.

########################################
print("------ DECRATORS ------")

def make_pretty(func):
    def inner():
        print("\nBEGIN decoration")
        func()
        print("END decoration")
    return inner

def ordinary():
    print("I am ordinary")


ordinary()
ordinary = make_pretty(ordinary)
ordinary()

########################################
# Simplified syntax
########################################
@make_pretty
def ordinary():
    print("I am ordinary")
# is equivalent to 
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)
########################################

################################################################################
# DECORATING WITH PARAMS
################################################################################
print("------ DECORATING WITH PARAMS ------")

# def divide(a, b):
#     return a/b

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide by zero")
            return
        else:
            return func(a, b)
    return inner

# equivalent to "divide = smart_divide(divide)"
@smart_divide
def divide(a,b):
    print(a/b)
    
divide(5,0)


# In Python, this magic is done as function(*args, **kwargs).
# *args will be the tuple of positional arguments
# **kwargs will be the dictionary of keyword arguments.
# example:
    
#     def works_for_all(func):
#         def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

@works_for_all
def multiply_by_four(a):
    a = a*4
    print(a)
    return a

multiply_by_four(4)

    