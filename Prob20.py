'''
Created on 2012-01-15

@author: Guigui
'''
import math

def projfunc():
    return sumDigits(get_100_fact())

def get_100_fact():
    return math.factorial(100)

def sumDigits(number):
    numStr = str(number)
    tot = 0
    
    for i in numStr: 
        tot += int(i)
    
    return tot

if __name__ == '__main__':
    print(projfunc())
