def printResult(counter, index, sList):
    print('counter: {}, index: {}, value: {}'.format(counter, index, sList[index]))
#
if __name__ == '__main__':
    sortedList = [i for i in range(1, 129)]
    find = 128
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
