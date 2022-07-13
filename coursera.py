# script - is a program simple, short, which is deployed rapidly.
# hard to find the bugs, therefore can't be used for the big infrastructure projects, but can be used to do small simple tasks.

print(4/3)
print(7 // 3)  # gives the integer part of division
print(7 % 3)
print(2**10)   # power operator
print(((2/3)**2) + 2)   # paranthesis for the work we want to do first.

# DATA TYPES
#string, integer, float

name = "parag"     # python is a case sensitive language, name and Name are two different variables
Name = "hello"
some_variable = None           # None is special keyword, is different from [], empty, true, false, it is just Null.
print(some_variable)
print(name)
print(Name)
val = 3
# print(3 + name)  gives error because unsupported function between two different types.
print(3 + 3.2)   # implicit type casting
print("hi " + name + " " + str(val))    # explicit type casting, integer to string


# Functions

def greet_persion(name):
	print("Welcome to python world " + name)

greet_persion("parag")
greet_persion("kyle")

def greet(name, age, gender):
	print("Hi " + name + " age is " + str(age) + " gender is " + gender)

greet("parag", 21, "male")

def fun(n):
	return n*n   # returning statements

val = fun(3)
print(val)

def fun2(n):
	name = "hello"
	ans = n*n
	return name, ans     # python can return more than one value
name, val = fun2(2)
print(name)
print(val)

# OPERATORS
a = 3
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b and a > b)
print(a == b or a < b)
print(not a == b)

# CONDITIONALS

if(a == b):
	print("a == b")
elif(a > b):
	print("a > b")
else:
	print("we are in else")

def is_even(n):
	if(n % 2):
		return False   # function exit after executing the return statement
	return True

print(is_even(8))


# LOOPS

x = 0
while(x < 5):
	if(x == 2):
		break  # breaking statements
	if(x == 1):
		x += 1
		continue
	print("The value of x is " + str(x))
	x += 1   # x = x+1 or x +=1 are the same thing
print("Loops exits the value of x is " + str(x))


for i in range(10):   # generate to 0 to n-1
	print(i, end = " ")   # end is to specify the last character of print statement, by default it is new line
print()
for i in range(1, 10):   # if there is a starting point, starting to end -1
	print(i, end = " ")
print()  # for new line

for i in range(0, 101, 10):   # starting to end - 1, with increment of 10 each time
	print(i, end = " ")
print()


# RECURSION
# recursion limit should be under 1000, if depth is greater than 1000, then recursion will not work
def rec_fun(n):
	if n < 2:    # Base condition
		return 1
	return n + rec_fun(n-1)

ans = rec_fun(100)
print(ans)



# DATA STRUCTURES IN PYTHON

# STRINGS - sequence of characters which are immutable(can't change)

# String, list and tuple are all sequence of character or data types, so they have a common thing in between like
# 1. Indexing - we can use index to go at certain position
# 2. For loop - we can traverse them by for loops
# 3. supports len function
# 4. operator '+' for concatenation
# 5. in keyword for checking certain value present in them or not.

fruit = "Mango"            # both are fine, the double quote and single quote
fruit = 'Mango'
# fruit[0] = 'K'         # we can't do this, because string are immutable
fruit = "Kango" # but we can replace the entire string
print(fruit[0], fruit[len(fruit)-1], fruit[-1])  # index can be negative in python, but it is better to not use them.

slice_mango = fruit[1:4]         # it return a substring from index start to end-1.
print(slice_mango)
slice_mango = fruit[:4]
print(slice_mango)
slice_mango = fruit[1:]
print(slice_mango)

complete_fruit = fruit[:3] + fruit[3:]
print(complete_fruit)

var = "  My name is parag is  "
print(var.index("is"))   # return the first occurence of that string
# print(var.index("kuch bhi"))  this will give Value Error, because this substring can't exist in string
print("kuch bhi" in var)   # so we have check this first, it return true or false

print(var.upper())
print(var.lower())
print(var.strip())   # to remove the extra front and end whitespaces

print(var.lstrip())
print(var.rstrip());

print(var.count("is"))  # return the number of time that substring comes in string

print(var.endswith("  "))  # return the true or false
var = "123423"
print(var.isnumeric())
print(int(var) + 322)
var = "This is my name"
string_by_list = "...".join(["This", "is", "my", "name"])
list_by_string = var.split()
print(list_by_string)
print(string_by_list)


#string formatting
example = "parag"
str = "This is my {}".format(example)
str = "This is my {var1}".format(var1 = example)  # need to specify explicitly
print(str)
str = "{:.2f}".format(10.432)
print(str)



# LISTS - is a sequence of any data type and they are mutable (can be changed)

my_list = ["This", "is", "my", "list", "is"]
print(len(my_list), my_list[0], my_list[1])
print("my" in my_list)
my_list = my_list + ["Hello"]
print(my_list)


my_list.append("another element")
my_list.insert(0, "inserting at 0th index")   # this will not overwrite the existing value, but shift all values.
print(my_list)

my_list.remove("is")   # remove first occurence of that string in the list, if exist otherwise gives error
if("is" in my_list):  # to avoid error
	print("it is there")

removed_element = my_list.pop(0)   # removes and return the 0th index element
my_list[0] = "To overite the 0th index value"
print(my_list)



# TUPLES - it is a list of any data type, but it is immutable(can't change)

my_tuple = ("harish", "M", "Gurgaon")
print(my_tuple, my_tuple[0])
# my_tuple[0] = "parag"  this is wrong as tuple are immutable
new = my_tuple + ("parag",)
print(new)

for index, val in enumerate(my_tuple):    # to get the index and value by enumeration
	print(index, val)


#List Comprehension - we can create the list by for loops but there is more convenient way to do the same i.e list comprehension

my_list = [x for x in range(1, 10)]
print(my_list)
my_list = [x for x in range(0, 21) if x % 2 == 0]
print(my_list)


#DICTIONARY   - map which are mutable

my_dict = {}
my_dict = {"jpg" : 10, "txt" : 32, "csv" : 22}
print(my_dict)
my_dict["cfg"] = 32
my_dict["csv"] = 23
print("html" in my_dict)
del my_dict["txt"]  # to delete the particular key
if "txtsa" in my_dict.keys():
	del my_dict["txtsa"]
print(my_dict)

my_dict = {"jpg" : 10, "txt" : 32, "csv" : 22, "cfg" : 10}
for key, value in my_dict.items():
	print(key, value, end = " ")

print()
print(my_dict.keys())
for key in my_dict.keys():
	print(key)
for value in my_dict.values():
	print(value)


print(len(my_dict))



# OBJECT ORIENTED PROGRAMMING

print(dir(name))   # used to show all methods associated to that data types
help(type(name))   # so show the complete details of a class

class Apple:
	# pass   # pass is the keyword we can use for any empty body thing
	color = "Yellow"
	flavor = "Soar"

jonagold = Apple()
jonagold.color = "RED"
jonagold.flavor = "Soar"

print(jonagold.color, jonagold.flavor, jonagold.flavor.upper())

class Piglet:       # for convention it is better to use Upper case for defining class
	name = "some random name"
	age = 0
	def speak(self):             # self is to get the current instance of class.
		print("Hi, I am {}".format(self.name))
	def setAge(self, age):    # we can't change the position of arguments
		self.age = age * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
print(hamlet.age)
hamlet.setAge(2)
print(hamlet.age)

class Apple:
	""" This is apple class and we can have color and flavor in it"""   # this is the docstring, which will return after we call help on this data type
	color = "yellow"
	flavor = "soar"
	def __init__(self, color, flavor):
		""" It initialise the instance with given color and flavor"""    
		self.color = color
		self.flavor = flavor
	def __str__(self):    # __str__ is a special method which works when we try to print the instance of class, by default it return the address of instance in the memory.
		""" It return the string on printing the instance of this class """
		return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


some_apple = Apple("red", "sweet")
print(some_apple.color, some_apple.flavor)
print(some_apple)  # __str__ invokes and return the string

help(Apple)    # docstring are really helpful for others to understand what your method and code is doing



#  CODE REUSE

# inheritance

class Fruit:
	color = "yellow"
	flavor = "soar"
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

class Apple(Fruit):    # parenthesis are used for showing inheritance
	pass
class Grape(Fruit):
	pass

class Orange(Fruit):
	size = 2

some_apple = Apple("red", "sweet")
some_grape = Grape("Green", "soar")
some_orange = Orange("Organe", "sweet")
print(some_apple.color, some_apple.flavor, some_grape.color, some_grape.flavor, some_orange.color, some_orange.flavor, some_orange.size)


class A:
	dicti = {}    # maybe these are called the class variables, they are different from self.dicti 
	def __init__(self, worms):
		# ALWAYS INITIALISE THE MUTABLE ATTRIBUTES IN THE CONSTRUCTOR OTHERWISE, ALL INSTANCE WILL SHARE THE SAME CLASS ATTRIBUTE
		self.dicti = {}
		self.dicti[worms] = 1

a1 = A("harish")
b1 = A("parag")
del a1.dicti["harish"]
print(a1.dicti, b1.dicti)

# Miscellinous, Functions

def fun(n, k, y):
	print(n, k, y)

fun(k = 1, n = 43, y = 11)   # another way of calling the function

def get_len(s):
	return len(s)

x = ["hi", "fad", "a"]
y = sorted(x, key = get_len, reverse = True)
print(y)

# Sets are immutable

my_set = set()

print(my_set)

x = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
print(type(x))