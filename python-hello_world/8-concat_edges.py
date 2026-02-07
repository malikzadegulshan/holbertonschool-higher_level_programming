#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str.split()
str = str[5:7] + [str[11]] + [str[0]]
str = chr(32).join(str)
print(str)
