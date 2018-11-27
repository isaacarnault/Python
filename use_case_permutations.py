# Calling the requested package and library
from math import factorial
def number_permutations(n, k):
  
# Defining permutations array of k items from a set of size n using the algorithm n!/(n-k)!
return factorial(n)/factorial(n-k)
q = '''\
How many ways can 4 aces from a standard 52-card deck
permutate while I shuffle the cards?
'''   
    
# Requesting the program output
print(q)
print(number_permutations(52, 4))

# Full program
from math import factorial
def number_permutations(n, k):
    return factorial(n)/factorial(n-k)
q = '''\
How many times can 4 aces from a standard 52-card deck
permutate while I shuffle the cards?
'''
print(q)
print(number_permutations(52, 4))
