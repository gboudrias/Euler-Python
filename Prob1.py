'''
Created on 2011-12-26

@author: Guigui
'''

def projfunc():
    totfunc = 0
    
    for i in range(1000):
        if ismult3(i) or ismult5(i):
            totfunc += i
    
    return totfunc

def ismult5(number):
    if number%5 == 0:
        return True
    else:
        return False

def ismult3(number):
    if number%3 == 0:
        return True
    else:
        return False

def addall(a_string):
    return sum(int(i) for i in str(a_string))    

if __name__ == '__main__':
    print(projfunc())