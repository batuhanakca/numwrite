#!/usr/bin/python
import random

#Create the Array
numbers = []
for i in range(1,11):
    numbers.append(i)

# Shuffle the array
random.shuffle(numbers)

#Print the Array
for x in range(len(numbers)):
  print (numbers[x])
