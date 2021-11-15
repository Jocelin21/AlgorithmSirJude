"""
write a program that given the name of a text file can write its content with each 
sentence on a separate line. Test your program with the following short text:
Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.
"""

import re
file = open("Miyagi.txt", "r")
file = file.read()
honor = ('(?<!Mr)(?<!Ms)(?<!Mrs)(?<!Dr)\. +(?=[A-Z])')
sentence = re.sub(honor,'.\n',file)

print (sentence)