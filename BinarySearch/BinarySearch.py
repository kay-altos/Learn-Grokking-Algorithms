#!/usr/bin/python3.8
#
import random

def printResult(counter, index, sList):
    print('find: {}, counter: {}, index: {}'.format(sList[index], counter, index))
#
if __name__ == '__main__':
    myList = [random.randint(1,100) + random.randint(1,10) for i in range(1, 11)]
    sortedList = sorted(myList)
    print('myList: {}\nsortedList: {}\n'.format(myList,sortedList))

    find = int(input('Enter Find: '))

    low, mid, high = 0,0,0
    counter = 0 
    high = len(sortedList) - 1 #0...n     
    #
    while mid != 1:
        counter += 1
        mid = ((high - low)//2) + low
        #
        if find == sortedList[low] or find == sortedList[high]:
            printResult(\
                    counter,\
                    low if find == sortedList[low] else high,\
                    sortedList)
            mid = 1
        if find == sortedList[mid]:
            printResult(counter, mid, sortedList)
            mid = 1
        if find > sortedList[mid]:
            low = mid + 1
        if find < sortedList[mid]:
            high = mid - 1
#
