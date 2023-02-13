# This Python script has been written for the course "Introduction to Python"
# at the University of Basel, Spring semester 2023
# Questions or suggestions ? leo.picard@unibas.ch


##############################################################################
# PYTHON ESSENTIALS
##############################################################################

# BASICS

# the command below is likely going to be the
# first thing you try in any programming language
print("Hello world!")


##############################################################################

# VARIABLES AND MULTIPLE ASSIGNMENT

# assign values to variables
number_1 = 15
my_name = "Leo"
num_list = [2, 5]

# delete them
del number_1, my_name, num_list

# assign them again
number_1, my_name, num_list = 15, "Leo", [2,5]


##############################################################################

# NUMBERS

number_1, number_2 = 1.99, 15
print(type(number_2))

number_2 = number_1 + number_2
print(type(number_2))


##############################################################################

# STRINGS AND F-STRINGS

"My name is ...", 'Python is fun!'

'He said, "I love my dog"'

name, birth = "Léo", 1995
sent = f"Hi ! My name is {name} and I'm {2023-birth} years old."

print(sent)


##############################################################################

# BOOLEANS

boolname = False
print(boolname)

boolname = (5**2 == 25)
print(boolname)


##############################################################################

# LISTS

listname = [1,4,5,8]
print(listname[2])

listname[2] = 7
print(listname)

a = [1,2]; a.append(3)
print(a)

a = [1,2]; a.insert(1,3)
print(a)

a = [1,2,3]; popped = a.pop(1)
print(a, popped)

a = [1,2]; b = a.copy()
print(a, b)

a = [4,1,5,3]; b = a.copy(); a.sort(); b.sort(reverse = True)
print(a, b)


##############################################################################

# SLICING LISTS

colors = ["red", "green", "blue", "yellow"]

print(colors[1:3]) # elements 1 and 2

print(colors[1:]) # last three elements

print(colors[-1:]) # first element


##############################################################################

# DICTIONARIES

dictname = {'BS': 'Basel Stadt', 'GE': 'Geneva', 'TI': 'Ticino'}
print(dictname['BS'])

dictname['ZH'] = "Zurich"
print(dictname)

dictname = {"owners": ("Antonia", "Elda"),
            "pets": {"dogs": ("Charlie", "Razmotte", "Nemo"),
                     "cats": ("Zazie", "Peps", "Zélie")}}

print(dictname["pets"]["dogs"])


##############################################################################

# ARITHMETIC OPERATORS

# addition
print(10 + 5)

# substraction
print(30 - 20)

# multiplication
print(2 * 5)

# division
print(6 / 2)

# modulus
print(10%4)

# exponent
print(2 ** 3)

# floor division
print(9 // 4)


##############################################################################

# COMPARISON OPERATORS

# equal
print(4 == 3)

# not equal
print(4 != 3)

# greater than
print(6 > 10)

# less than
print(2 < 5)

# greater or equal than
print(8 >= 3)

# less or equal than
print(5 <= 5)


##############################################################################

# BOOLEAN OPERATORS

x = True; y = False

print(x or y)

print(x and y)

print(not x)


##############################################################################

# IF STATEMENTS

x, y = 5, 10

if y < x:
	print("y smaller than x")
else:
	print("y greater than x")


##############################################################################

# FOR LOOPS

numbers = [4,34,2]

for number in numbers:
	print(number + 1)


##############################################################################

# LIST COMPREHENSION

listname = [1, 2, 3, 4, 5, 6]

listname = [x*x for x in listname]
print(listname)

# we can even add conditions
listname = [x for x in listname if x%2 == 0]
print(listname)


##############################################################################

# HOW MANY LOOPS ?

for i in range(1, 4):
	print("Loop number", i)


floats = [1.2, 2.343, 0.44]

for i in range(len(floats)):
	print(i, floats[i])

# another example with list COMPREHENSION
list_loop = [2*i for i in range(5)]
print(list_loop)


##############################################################################

# WHILE LOOPS

i = 1
while i < 10:
	print(i)
	if i == 4:
		break
	i += 1 # equivalent to i = i + 1


#############################################################################

# FUNCTIONS

def fib(n):
	"""Print a Fibonacci series up to n"""
	a, b = 0, 1
	while a < n:
		print(a, end = ' ')
		a, b = b, a + b

fib(10)

def squared(array):
    """
    find the square of each element in a vector
    """
    output = []
    for elem in array:
        elem_squared = elem**2
        output.append(elem_squared)
    return output

n = [2, 5, 10]
n_squared = squared(n)

print(n_squared)