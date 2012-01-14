'''
Created on 2011-12-27

@author: Guigui
'''

def projfunc():
    for a in range(1,999):
        for b in range(2,999):
            for c in range(3,999):
                if a + b + c == 1000:
                    print(str(a**2*b**2) + ' = ' + str(c**2))
                    if a**2 + b**2 == c** 2:
                        return str(a) + ' ' + str(b) + ' ' + str(c)
    
    return False

if __name__ == '__main__':
    print(projfunc())