'''
Created on 2011-12-27

@author: Guigui
'''

def projfunc():
    biggestPal = 0
    biggestI = 0
    biggestJ = 0
    
    for i in range(900, 1000):
        for j in range(900, 1000):
            number = j*i
            if isPalindrome(number) and number > biggestPal:
                biggestI = i
                biggestJ = j
                biggestPal = number
                
    return biggestPal
            
def isPalindrome(number):
    strNum = str(number)
    strRev = strNum[::-1]
    
    return (strNum == strRev) 

if __name__ == '__main__':
    print(projfunc())