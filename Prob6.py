'''
Created on 2011-12-27

@author: Guigui
'''

import math

def projfunc():
    number = 100
    
    sumSquare = getSumSquare(number)
    squareSum = addSquares(number)
    
    return sumSquare - squareSum

def addSquares(number):
    total = 0
    
    for i in range(1, number + 1):
        total += math.pow(i, 2)
        
    return total
            
def getSumSquare(number):
    total = 0
    
    for i in range(1, number + 1):
        total += i
        
    return math.pow(total, 2)

if __name__ == '__main__':
    print(str(projfunc()))