# Permutations using Python

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

One simple program using Python for applying strings and integer permutations.<br>
The following gist offers a program scaled in four subsets:
* apply permutations on strings, refer to <b>strings_permutation.py</b>
* apply permutations on integers, refer to <b>integers_permutation.py</b>
* apply permutations on both integers and strings in a single program, refer to <b>integers_strings_permutation.py</b>
* use case: apply permutations on a card game, refer to <b>use_case_permutations.py</b>.

## Getting Started

This Python program built in four lines helps you avoid the use of an extented code for applying permutations on numeric data.
The below instructions will help you run this Python program on your local machine for development and testing purposes, as well as in third party sites hosted in the cloud.
* (#) and (''') are used to comment the following gist.

### Prerequisites

I am using Jupyter Notebook on localhost (Ubuntu 18.04 bionic).<br>
Make sure to have Jupyter Notebook installed on your operating system or launch it on remote servers (see Tips).

### Tips

If you are not using Linux/Unix and still want to try this simple Python program:
* use https://labs.cognitiveclass.ai (create a free account, then click on "JupyterLab" in the Build Analytics section)
* use https://dataplatform.ibm.com (recommended for IBM Coders)

### Basic commands in Jupyter Notebook

* Note that in Jupyter you add new lines by typing "b" from your keyboard whilst the notebook is opened.
* Avoid runing the entire code in a single cell in  order to understand the steps.
* Use "ctrl + enter" to execute each line if you want to get the output.
* Use "dd" outside a cell to delete it.
* Running the last cell should execute the permutations as program output.

Whilst your Jupyter Notebook is open...
Use this line of code in your first cell
```
from itertools import permutations

'''
This loads requested package
and library in your notebook
'''
```

Use this line of code in your second cell
```
perm = permutations([3, 6, 9])

'''
This returns no result until
the last cell is ran
'''
```

Use this line of code in your third cell
```
for (i) in list(perm): 
print (i)

'''
This completes the program, showing permutations
of numbers 3,6,9 as output.
'''
```

## Running the tests

* I used Ubuntu (18.04 bionic) to launch Jupyter Notebook on localhost.
* Localhost instantiates while using <b>$ jupyter notebook</b> in the terminal.
* Check if Jupyter is correctly installed: <b>$ jupyter --version</b>

## Built With

* [Jupyter](http://jupyter.org/) - An open source software for creating notebooks
* [Itertools](https://docs.python.org/3/library/itertools.html) - Functions creating iterators for efficient looping
* [Math](https://docs.python.org/3/library/itertools.html) - Mathematical functions defined by the C standar

## Versioning

I used no vesioning system for this gist. My repository's status is flagged as <b>active</b> because it has reached a stable, usable state. Original [gist](https://gist.github.com/aiPhD/f4cdef7878e88ee2bed1254a2b5fbcb5) related to this repository is pending as <b>concept</b>.

## Author

* **Isaac Arnault** - Suggesting a minified code from *Initial work* [redspider](https://gist.github.com/redspider/3787386)

## License

All public gists https://gist.github.com/aiPhD<br>
Copyright 2018, Isaac Arnault<br>
MIT License, http://www.opensource.org/licenses/mit-license.php

## Use case - Applying a <i>factorial n</i> function in a card game

Extended application of the above program. Permutations are great for finding number of ways an array of integers can be sorted. Let's imagine that that we have a standard 52-card deck and we wish to find the number of permutations of four aces while shuffling the cards. We may need to add a function to our code and to use another package and libraby. Check <b>use_case_permutations.py</b> for more info.
