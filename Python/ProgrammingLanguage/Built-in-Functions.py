
# Return the absolute value
print(abs(-2.45345))

# Return true if all iterable is true
print(all([True, True, True, True]))

# Return true if any of iterable is true
print(any([True, False, None, False]))

# Convert integer number to binary string prefixed with '0b'
print(bin(123))

# Return string representing a character
print(chr(100))
print(ord('d'))

# Used to retorn the properties of a class
print(dir())

# Used to enumerate a list of objects
print(list(enumerate(['test', 'horse', 'drink'])))

# Execute a specific python code
exec('name = 1\nprint(name)')

# Used to filter something
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)

for s in filtered:
    print(s)

# Convert integer number to hexadecimal string
print(hex(123))

# Receive a input data from user
#print(input('-- > '))

# Return the length of a string or a object
print(len([1, 3, 6, 7, 4]))

# Return number rounded
print(round(2.534534))

# Sort a list
print(sorted([9,43,87,32,8,35]))

# Sums the items from left to right
print(sum([1, 2, 3, 4, 5]))

# Return the type of a object
print(type('gdfngk'))