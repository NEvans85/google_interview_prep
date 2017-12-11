"""
Quicksort is a sorting algorithm with an average complexity of O(n*log(n)).
It works by choosing a pivot element, seperating the remaining elements into
a list of values less then the pivot and a list of elements greater then the 
element, then performing quicksort on the left (less than) and right (greater than) 
elements. Using this recursive algorithm, each step takes O(n) and the number of 
steps is logarithmically related to the number of elements. The following 
implementation uses the first element as the pivot. The worst case scenario for 
this implementation is a list which is already sorted or in reverse order, causing
all the elements to end up in either the left or right list for each iteraion. This 
would require n steps, resulting in a complexity of O(n**2).
"""

def quicksort(iList):
    left = []
    right = []
    pivotList = []
    if len(iList) <= 1:
        return iList
    else:
        pivot = iList[0]
        for el in iList:
            if el < pivot:
                left.append(el)
            elif el > pivot:
                right.append(el)
            else:
                pivotList.append(el)
        left = quicksort(left)
        right = quicksort(right)
        return left + pivotList + right
    