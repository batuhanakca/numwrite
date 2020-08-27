#!/usr/bin/env python3
import random
import argparse

def main():
    parser = argparse.ArgumentParser(usage='''
              %(prog)s <end> <start>    : Default numbers are 1 to 10
              %(prog)s                  : print numbers from 1 to 10 randomly
              %(prog)s 5                : print numbers from 1 to 5 randomly 
              %(prog)s 15 3             : print numbers from 3 to 15 randomly 
        ''') 
   
    parser.add_argument('end', help="End in this number", nargs='?', type=int, const=1, default=10)
    parser.add_argument('start', help="Start from this number", nargs='?', type=int, const=1, default=1)

    args = parser.parse_args()

    X = args.start
    Y = args.end + 1

    def numWriter(a,b):
        #Create the Array
        numbers = []
        for i in range(a,b):
            numbers.append(i)

        # Shuffle the array
        random.shuffle(numbers)

        #Print the Array
        for x in range(len(numbers)):
            print (numbers[x])
    
    if ( X < Y ):
        numWriter(X,Y)
    else:
        print ("Start Number should be smaller than end number")
        print ("I think you made a typo, still will generate your numbers")
        print ("Write the numbers in order Next time. If you don't want to see this message")
        numWriter(Y,X)
main()
