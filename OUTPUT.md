Ignore below outputs if programs ran correctly.<br>
If you begin in `Python` using `Jupyter` these are what you should get:

* apply permutations on strings, see <b>strings_permutation.py</b>
<details><summary>strings_permutation</summary>
<p>
  
```python
# Full program
from itertools import permutations
perm = permutations(['Insta', 'Snap', 'Twitter'])    
for (i) in list(perm):
  print (i)
```

</p>
</details>

[![isaac-arnault-python-strings-permutation.png](https://i.postimg.cc/jjmmw7sR/isaac-arnault-python-strings-permutation.png)](https://postimg.cc/zLw043bQ)

* apply permutations on integers, see <b>integers_permutation.py</b>
<details><summary>integers_permutation</summary>
<p>
  
```python
# Full program
from itertools import permutations
perm = permutations([3, 6, 9])    
for (i) in list(perm):
  print (i)
```

</p>
</details>

[![isaac-arnault-integers-permutations.png](https://i.postimg.cc/0jLLTKBt/isaac-arnault-integers-permutations.png)](https://postimg.cc/JH56J0mJ)

* apply permutations on both integers and strings in a single program, see <b>integers_strings_permutation.py</b>
<details><summary>integers_strings_permutation</summary>
<p>
  
```python
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
```

</p>
</details>

[![isaac-arnault-python-integers-strings-permutations.png](https://i.postimg.cc/mDBJghXY/isaac-arnault-python-integers-strings-permutations.png)](https://postimg.cc/Y4DbX2w0)

* use case: apply permutations on a card game, see <b>use_case_permutations.py</b>
<details><summary>use_case_permutations</summary>
<p>
  
```python
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
```

</p>
</details>

[![isaac-arnault-use-case-permutations.png](https://i.postimg.cc/26XQ8Qmx/isaac-arnault-use-case-permutations.png)](https://postimg.cc/PpYpS8CL)
