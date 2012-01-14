'''
Created on 2012-01-04

@author: Guigui
'''

def projfunc():
    number = 2**1000
    
    return sumDigits(number)

def sumDigits(number):
    numStr = str(number)
    tot = 0
    
    for i in numStr: 
        tot += int(i)
    
    return tot
    
if __name__ == '__main__':
    print(projfunc())