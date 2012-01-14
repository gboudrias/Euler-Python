'''
Created on 2012-01-03

@author: Guigui
'''

import math

def projfunc():
    return firstTriangleWithNFactors(5)

def firstTriangleWithNFactors(n):
    factors = 0
    
    i = 1
    while factors < n:
        triangle = getTriangle(i)
        factors = find_factors(triangle, triangle)
        
        print(str(i) + 'nth: ' + str(triangle) + ' : ' + str(factors))
        
        i += 1
        
    return triangle

def getTriangle(nth):
    total = 0
    
    for i in range(1, nth + 1):
        total += i
        
    return total

def find_factors(n1, n2):
    factors = []
    i=2
    n4=1
   
    ##find all the prime factors of the number
    while i <= n1:

        if n1%i==0:
            factors.append(i)
            n1/=i

        else:

            i+=1

    ##finds the power each prime factor is raised to to get the number
    explist=[0 for j in range(0,len(factors))]

    for k in range (0, len(explist)):
   
        while n2%factors[k]==0:
            n2/=factors[k]
            explist[k]+=1

    ##removes duplicate factor values from factors and 0 values from explist
    while 0 in explist:

        n4=explist.index(0)
        del factors[n4]
        del explist[n4]

    ##finds the total number of factors of the number (prime and composite)
    for l in range (0, len(explist)):
        n4 = n4*(explist[l]+1)

    return n4

def triangle_numbers():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1

def prime_factorization(n):
    candidate_factor = 2
    while n > 1:
        factors = []
        while n % candidate_factor == 0:
            factors.append(candidate_factor)
            n /= candidate_factor
        if factors:
            yield factors
        candidate_factor += 1

def count_divisors(n):
    count = 1
    for tuple in prime_factorization(n):
        count *= (len(tuple) + 1) 
    return count
            
if __name__ == '__main__':
    for t in triangle_numbers():
        if count_divisors(t) > 500:
            print(t)
            break
    #print(projfunc())