'''
Created on 2011-12-26

@author: Guigui
'''

def projfunc():
    return largestPrimeFactor(600851475143)

def largestPrimeFactor(number):
    i = 2

    while i <= number:
        if number % i == 0:
            number /= i
            i -= 1
        
        i += 1
        
    return i

if __name__ == '__main__':
    print(projfunc())