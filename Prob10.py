'''
Created on 2011-12-27

@author: Guigui
'''

def projfunc():
    sumfunc = 0
    
    for i in range(2, 2000000):
        if isPrime(i):
            sumfunc += i
            
        if i%10000 == 0:
            print(i)
    
    return sumfunc
    
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