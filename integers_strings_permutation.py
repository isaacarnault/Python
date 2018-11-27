# Calling two packages and a related library per each
from itertools import permutations
from math import factorial

# Defining permutations array of strings
perm = permutations(['Insta', 'Snap', 'Twitter']) 

# Requesting the program to ask a question (q1) and print the result (program will compile the array of strings)
q1 = '''\ 
Which permutations do I make using three social networks?
'''
print(q1)
for (i) in list(perm):
  print (i)
  
# Removing print() from your program will just remove the blank line between both questions without affecting the entire program
print() 

# Requesting the program to ask a question (q2) and print the result (program will compile the array of integers)
q2 = '''\
How many times do I permute using three social networks?
'''
print(q2)
def number_permutations(n, k):
     return factorial(n)/factorial(n-k)
print(number_permutations(3, 3))

# Full program
from itertools import permutations
from math import factorial
perm = permutations(['Insta', 'Snap', 'Twitter']) 
q1 = '''\
Which permutations do I make using three social networks?
'''
print(q1)
for (i) in list(perm):
  print (i)
print() 
q2 = '''\
How many times do I permute using three social networks?
'''
print(q2)
def number_permutations(n, k):
     return factorial(n)/factorial(n-k)
print(number_permutations(3, 3))
