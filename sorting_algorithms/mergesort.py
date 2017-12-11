"""
Mergesort is a sorting algorithm with a time complexity of O(n*log(n)). It works by
splitting a list of comparable elements in half until they are single elemts lists
then combining those lists, sorting along the way. This is accomplished with a 
recursive mergesort function which splits up the elements then uses a merge
function. The merge function takes in two lists and evaluates them, combining them
in a sorted order. 
"""

def mergesort(iList):
    if len(iList) <= 1:
        return iList
    middle = len(iList) // 2
    left = iList[:middle]
    right = iList[middle:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
    
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if len(left) > 0:
        result += left
    else:
        result += right
    return result
            
        
        