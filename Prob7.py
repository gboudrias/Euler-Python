'''
Created on 2011-12-27

@author: Guigui
'''

def projfunc():
    return getNthPrime(10001)

def getNthPrime(n):
    totalPrimes = 0
    
    i = 0
    while totalPrimes < n:
        i += 1
        if isPrime(i):
            totalPrimes += 1
            
            print(str(totalPrimes) + "th prime: " + str(i))
            
            if totalPrimes == n:
                return i

def isPrime(n):
    if n == 1:
        return 0
    else:
        for x in range(2,int(n**0.5)+1):
            if n%x == 0:
                return False
        
        return True
            
if __name__ == '__main__':
    print(projfunc())