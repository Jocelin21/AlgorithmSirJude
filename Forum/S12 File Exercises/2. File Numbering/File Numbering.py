"""
Write a program that given a text file will create a new text 
file in which all the lines from the original file are numbered 
from 1 to n (where n is the number of lines in the file).
"""
numbering = open("numbering.txt", 'r')
number = open("Number.txt", 'w')

count = 0
for i in numbering:
    count += 1
    number.write(f"{count} {i}")
number.close()