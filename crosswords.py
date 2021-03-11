'''
Create a function that takes in two strings. Find the intersections of common 
Formula for enclosed area (w-1)*(h-1) - setup for a function to do calculations
'''

__author__ = "ChaoticNite"

'''
Test Strings:
OIMDIHEIAFNL
CHJDBJMHPJKD
'''

import re

WORD_ONE = "OIMDIHEIAFNL"
WORD_TWO = "CHJDBJMHPJKD"

def word_sets(word_one, word_two):
    tuple_set = []
    for i, letter in enumerate(word_one):
        for x in re.finditer(letter, word_two):
            tuple_set.append(tuple((i, x.start())))
    result = sort_func(tups=tuple_set, frst_word=word_one, scnd_word=word_two)
    return result

def sort_func(tups, frst_word, scnd_word):
    list_of_tups = []
    for tup in tups:
        frst_index, scnd_index = tup[0], tup[1]
        if frst_index > len(frst_word) // 2:
            frst_index = abs(frst_index - len(frst_word))
        if scnd_index > len(scnd_word) // 2:
            scnd_index = abs(scnd_index - len(scnd_word)) 


print(word_sets(WORD_ONE, WORD_TWO))