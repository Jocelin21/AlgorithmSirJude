"""
Write a program that will calculate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
"""

import re

def average(path):
    file = open(path)
    words = re.findall('\w+', file.read())
    avg = round(sum([len(word) for word in words]) / len(words))
    print("The average word length is", avg)

average('Tunnel.txt')
