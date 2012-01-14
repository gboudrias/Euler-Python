'''
Created on 2011-12-26

@author: Guigui
'''

def projfunc():
    print(11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20)
    return smallestEvenDiv(20)

def smallestEvenDiv(bigDiv, start = -1):
    dividers = list(range(2, bigDiv + 1))
    
    for i in range(bigDiv, 2, -1):
        for j in dividers:
            if i % j == 0 and i != j:
                dividers.remove(j)
                
    if start == -1:
        number = bigDiv
    else:
        number = start
    
    print("Dividers: " + str(dividers))
    print("Starting at: " + str(number) + ", counting up")
    
    while True:
        number += 1
        found = True
        
        for i in dividers:
            if number % i != 0:
                found = False
                continue
        
        if number % 1000000 == 0:
            print(str(number))
        
        if found == True:
            print("FOUND")
            break
    
    return number


# NOT MINE
def is_divisible_to(number, x):
    for i in reversed(range(1, x+1)):
        if number % i != 0:
            return False
    return True

def divisible_to(x):
    if x < 1:
        return False
    elif x == 1:
        return 1
    else:
        step = divisible_to(x-1)
        number = 0
        found = False
        while not found:
            number += step
            found = is_divisible_to(number, x)
        return number

            
if __name__ == '__main__':
    print(str(divisible_to(20)))
    
    #print(projfunc())