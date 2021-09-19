# Use joins for adding items onto lists
    
# Don’t do this:
mymsg='line1\n'
mymsg+='line2\n'

# Better choice:
mymsg=['line1','line2']
'\n'.join(mymsg)

# Avoid using the + operator for strings

# Don’t do this:
text='simple text'
msg='hello'+text+'world'

# Better choice:
msg='hello %s world' % mymsg

# Use Generators
def __iter__(self):
     return self._generator()
def _generator(self):
     for itm in self.items():
         yield itm

# Put evaluations outside the loop
import regex as re
match_regex=re.compile('foo|bar')
big_it=['teste', 'teste1', 'foo']
for i in big_it:
     m = match_regex.search(i)
     print(m)

# Use built-in functions and libraries
# Don’t do this:
mylist=[]
for myword in oldlist:
      mylist.append(myword.upper())

#Better choice:
mylist=map(str.lower, oldlist)
