'''
Created on 2012-01-13

@author: Guigui
'''

def projfunc():
    return getFact(40) / getFact(20) / getFact(20)

def getFact(n):
    tot = 1
    for i in range(1, n+1): 
        tot = tot * i
        
    return tot
            
if __name__ == '__main__':
    print(projfunc())