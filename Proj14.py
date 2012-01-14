'''
Created on 2012-01-13

@author: Guigui
'''

def projfunc():
    maxNum = 1000000
    
    maxChainer = 1
    maxChain = 0
    
    for i in range(maxNum, 2, -1):
        tmpTot = countChain(i)
        if tmpTot > maxChain:
            maxChain = tmpTot
            maxChainer = i
            print("Maxchainer: " + str(maxChainer) + ", length: " + str(maxChain))
    
    return maxChainer
            
def countChain(n):
    total = 1
    
    while n != 1:
        n = getNext(n)
        total += 1
    
    return total
    
def getNext(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return n*3 + 1

if __name__ == '__main__':
    print(projfunc())