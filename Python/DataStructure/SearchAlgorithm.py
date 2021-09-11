
# Membership Operator
print('apple' in ['orange', 'apple', 'grape'])
print('q' not in 'stackbuse')

# Linear Search
def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1