
# Membership Operator
print('apple' in ['orange', 'apple', 'grape'])
print('q' not in 'stackbuse')

# Linear Search
def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

print(LinearSearch([1,2,3,4,5,2,1], 2))

# Binary search
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([10,20,30,40,50], 20))

