'''
Created on 2011-12-26

@author: Guigui
'''

import time

# prob 364

def projfunc():
    
    
    """ benchmarking
    lastTime = 0
    for i in range(2,14):
        t1 = time.time()
        getNumberOfWays(i)
        t2 = time.time()
        newTime = t2-t1
        
        if lastTime != 0.0:
            print(str(i) + ' ' + str(newTime))
        
        lastTime = newTime
            
    """

    rowWidth = 9

    for i in range(0, rowWidth):
        print('Col' + str(i) + ': ' + str(getNumberOfWays(rowWidth, i)))
    
    return ""

def getNumberOfWays(seats, cond = -1):
    row = []
    
    for i in range(0,seats):
        row.append(0)
    
    totalNow = 0
    
    for i in getValidSeats(row):
        totalNow += getNumberOfSeatGrabs(i, row, 0, i, cond)
    
    return totalNow

def getNumberOfSeatGrabs(startingPos, oldRow, totalYet, initialStart, ex = -1):    
    row = list(oldRow)
    
    row[startingPos] = 1
    
    totalNow = 0

    if isRowFull(row) != True:
        for i in getValidSeats(row):
            totalNow += getNumberOfSeatGrabs(i, row, totalYet, initialStart, ex)
    else:
        if ex == -1:
            return 1
        # pos
        else:
            if initialStart == ex:
                return 1
            else:
                return 0            
    
    return totalNow

'''
If there is any seat whose adjacent seat(s) are not occupied take such a seat.
If there is no such seat and there is any seat for which only one adjacent seat is occupied take such a seat.
Otherwise take one of the remaining available seats.
'''
def getValidSeats(row):
    if isRowFull(row):
        return []
    
    listOfSeats = []

    ''' If there is any seat whose adjacent seat(s) are not occupied take such a seat.'''    
    for i in range(0,len(row)):
        if row[i] == 0:
            ''' Obviously, taken seat is invalid '''
            if i == 0:
                '''Edge case left '''
                if row[i + 1] == 0:
                    listOfSeats.append(i)
            elif i == len(row) -1:
                ''' Edge case right '''
                if row[i - 1] == 0:
                    listOfSeats.append(i)
            else:
                ''' Not an edge case '''
                if row[i - 1] == 0 and row[i + 1] == 0:
                    listOfSeats.append(i)

    if len(listOfSeats) > 0:
        return listOfSeats

    ''' If there is no such seat and there is any seat for which only one adjacent seat is occupied take such a seat. '''
    for i in range(0,len(row)):
        if row[i] == 0:
            ''' Obviously, taken seat is invalid '''
            if i == 0:
                '''Edge case left, left is always open '''
                listOfSeats.append(i)
            elif i == len(row) -1:
                ''' Edge case right, right is always open '''
                listOfSeats.append(i)
            else:
                ''' Not an edge case '''
                if row[i - 1] == 0 or row[i + 1] == 0:
                    listOfSeats.append(i)

    if len(listOfSeats) > 0:
        return listOfSeats
    
    for i in range(0,len(row)):
        if row[i] == 0:
            listOfSeats.append(i)
    
    return listOfSeats

def isRowFull(row):
    for i in row:
        if i == 0:
            return False
    
    return True

if __name__ == '__main__':
    print(projfunc())
    print('')