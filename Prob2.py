'''
Created on 2011-12-26

@author: Guigui
'''

def projfunc():
    totfunc = 0
    
    for i in getFibb(4000000):
        if i%2 == 0:
            totfunc += i
    
    return totfunc

def getFibb(upperlimit):
    sequence=[1,2]
    i = 2

    while True:
        i = sequence[-1] + sequence[-2]
        
        if i < upperlimit:
            sequence.append(i)
        else:
            break
        
    return sequence

if __name__ == '__main__':
    print(projfunc())