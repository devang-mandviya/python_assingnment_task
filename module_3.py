menu = """
Q.1)What is List? How will you reverse a list?
ANS.
>>    List is a collection of data type which is contain similar and dis-similar data type elements.
>>    List is represent by [] .
>>    List is orderable , indexable , list can contain duplicate element .
>>    List is mutable (changeable).
>>    List index always start from 0 .
>>    Reversing the list here refer to directly modify the original list elements rather than creating a new list and copy the elements there in reverse order.


Q.2)How will you remove last object from a list ?
    Support list 1 is [2,33,222,14, and 25], what is list1 [-1] ?
ANS. 
>>    Python provide a provision for slicing the lists using the subscript operators . For slicing a list, one needs to provide the starting and ending index in the subscript operator.
           list [start:end]


Q.3)Differentiate between append () and extend () methods?
ANS. 
                      Extand()                           |                Append()
---------------------------------------------------------|----------------------------------------------------
>> Each element of the iterable passed as an             |        >> The element passsed as an argument is append to
   argument gets appended to the end of the list.        |           the end of the list.
    ----------------------------------------------       |        -----------------------------------------------------------
>> An iterable passed as an argument will append         |        >> An iterable passed as an argument append witout
   each of its elements to the end of the list.          |            any change as a single element to the end of the list.
    ----------------------------------------------       |        -----------------------------------------------------------
>> Length of the list increases by the number of         |        >> Length of the list increases by 1.
   element in the iterable .                             |        
    ----------------------------------------------       |        -----------------------------------------------------------
>> Has a time complexity of 0(k) where k is the          |        >> Has a constant time complexity of 0(1).
   length of the iterable                                |
"""
print (menu)
print ("--------------------------------------------- QUESTION - 2 -----------------------------------------")
print (">> Support list 1 is [2,33,222,14, and 25]and remove last elements")
# program to delete the last object from list 
line1= [2,33,222,14,25]
print ("orignal list =",line1)
line2 = line1 [:-1]
print ("update list :",line2)

print ("--------------------------------------------- QUESTION - 4 -----------------------------------------")
print (">> Write a Python function to get the largest number, smallest num and sum of all from a list.")
# find largest number and smallest number 
# sum of all element in list 
l1 = [11,22,33,44,55,66,77,88,99]
print (l1)
print ("Large number in list :",max(l1))
print ("smallest number in list :",min(l1))
mm = sum(l1)
print ("sum of all element in list =",mm)

menu2="""
Q.5) How will you compare two lists?
ANS.
>>  We will understand the different ways to compare two lists in python.We often come across situations Where
    we need to compare the values the data item stored in any structure say list,tuple,string,etc.

>>  comparison is the method of checking the data item of a list against equality with data items of the 
    another list .
"""
print(menu2)

print ("------------------------------------- QUESTION - 7 --------------------------------------------------")
print (">>  Write a Python program to remove duplicates from a list.")
# remove duplicate in list 
number1 = [2,3,4,5,5,2,4,67,8,9,3,46,78,3,4,2,41]
number2=set(number1)
print ("list :",number1)
print (list(number2))

print ("------------------------------------- QUESTION - 8 --------------------------------------------------")
print (">>  Write a Python program to check a list is empty or not.")
# cherck list empty or not 
my_list = []
if len (my_list) == 0:
    print ("list is empty")
else:
    print ("list is not empty")

print ("------------------------------------- QUESTION - 9 --------------------------------------------------") 
print (">>  Write a Python function that takes two lists and returns true if they have at least one common member.")
# take two list and return value 
def l1(nums, lsts):
    for x in lsts:
        if x in nums:
            return True
    return False    
print(l1([10, 20, 30, 40, 50, 60], [22, 42]))
print(l1([10, 20, 30, 40, 50, 60], [20, 80]))

print("-------------------------------------- QUESTION - 10 -------------------------------------------------")
print ("Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.")
# square number fisrt and last 5 object  
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])
printValues()

print ("------------------------------------- QUESTION - 11 ------------------------------------------------")
print ("Write a Python function that takes a list and returns a new list with unique elements of the first list.")
# returns duplicate elements 
# and out unique list 
def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print(unique_list([1,2,4,5,4,5,6,9,10]))

print ("------------------------------------- QUESTION - 12 ------------------------------------------------")
print ("Write a Python program to convert a list of characters into a string.")
# charcters list convert to string 
def convert(s):
	d = ""
	for x in s:
		d += x
	return d
s = ['D', 'E', 'V', 'A', 'N', 'G']
print (s)
print(convert(s))

print ("------------------------------------- QUESTION - 13 -------------------------------------------------")
print ("Write a Python program to select an item randomly from a list.")
# select item rendomly
import random
import string
name_list= ['dev', 'avi', 'tanvi']
print (name_list)
print(random.choice(name_list))


print ("------------------------------------- QUESTION - 14 ------------------------------------------------")
print ("Write a Python program to find the second smallest number in a list.")
# find second smallest number in list 
def find_len(list1):
	list1.sort()
	print("Second Smallest element is:", list1[1])
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
print(list1)
small = find_len(list1)

print("-------------------------------------- QUESTION - 15 -------------------------------------------------")
print ("Write a Python program to get unique values from a list")
# unique value for list
def unique(list1):
	unique_list = []
	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	for x in unique_list:
		    print (x)
list1 = [10, 20, 10, 30, 10, 40, 40]
print("the unique values from 1st list is")
unique(list1)

print ("-------------------------------------- QUESTION - 16 ------------------------------------------------")
print ("Write a Python program to check whether a list contains a sub list")
# list check containts a sub list 
def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				if n == len(s):
					sub_set = True
	return sub_set
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

print ("----------------------------------------- QUESTION - 17 ----------------------------------------------")
print ("Write a Python program to split a list into different variables.")
# split into variable 
name = [("Devang", "Mandviya"), ("Avi","Parekh"),]
var1, var2 = name
print ("old list :",name)
print(var1)
print(var2)

menu3="""
Q.18) What is tuple? Difference between list and tuple.
ANS. 
	Tuple :
		>>	A tuple is a sequence of immutable Python objects.
		>>	Tuples are sequences, just like lists.
		>>	The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

		>>	Diffrent between list and tuple >>

                          LIST                          |                    TUPLE 
--------------------------------------------------------|---------------------------------------------------------------------
>>  Lists are mutable.                                  |>>	Tuples are immutable.
    --------------------------------------------        |	----------------------------------------------
>>  The implication of iterations is Time-consuming.    |>>	The implication of iterations is comparatively Faster.
    --------------------------------------------        |	----------------------------------------------
>>  The list is better for performing operations,       |>>	Tuple data type is appropriate for accessing 
    such as insertion and deletion.                     |	the elements.
    --------------------------------------------        |	----------------------------------------------	
>>  Lists consume more memory.                          |>>	Tuple consumes less memory as compared to the list.
    --------------------------------------------        |	-----------------------------------------------
>>  Lists have several built-in methods.                |>>  Tuple does not have many built-in methods.
    --------------------------------------------        |	------------------------------------------------
>>  The unexpected changes and errors are               |>>	In tuple, it is hard to take place.
    more likely to occur                                |
--------------------------------------------------------|-----------------------------------------------------------------------
"""
print (menu3)

print ("------------------------------------------ QUESTION - 19 ----------------------------------------------")
print ("Write a Python program to create a tuple with different data types.")
#Create a tuple with different data types
data = ("tuple", False, 22, 5)
print(data)

print ("------------------------------------------ QUESTION - 20 ----------------------------------------------")
print ("Write a Python program to create a tuple with numbers.")
#Create a tuple with numbers
num = 2, 4, 6, 8,10
print(num)
tuplex = 4
print(tuplex)

print ("------------------------------------------- QUESTION - 21 ----------------------------------------------")
print ("write a Python program to convert a tuple to a string.")
# Python3 code to convert a tuple
# into a string using a for loop
def convertTuple(tup):
	dd = ''
	for item in tup:
		dd = dd + item
	return dd
chr = ('D', 'E', 'V', 'A', 'N' ,'G')
dd = convertTuple(chr)
print(dd)

print ("------------------------------------------- QUESTION - 22 ----------------------------------------------")
print ("write a Python program to check whether an element exists within a tuple.")
# check element exixst in tuple 
tuplex = ("T", 0, "P", "S")
print("T" in tuplex)
print(2 in tuplex)

print ("------------------------------------------- QUESTION - 23 ----------------------------------------------")
print ("Write a Python program to find the length of a tuple.")
# find tuple length
name= (tuple("python"))
print(name)
print(len(name))

print ("------------------------------------------- QUESTION - 24 ----------------------------------------------")
print ("Write a Python program to convert a list to a tuple.")
#Convert list to tuple
number = [5, 10, 7, 4, 15, 3]
print(number)
new_num = (tuple(number))
print(new_num)

print ("------------------------------------------- QUESTION - 25 ----------------------------------------------")
print ("Write a Python program to reverse a tuple.")
# reverse of tuple 
x = (1,2,3,4,5,6,7,8,9,0)
# Reversed the tuple
y = reversed(x)
print(tuple(y))

print ("------------------------------------------- QUESTION - 26 ----------------------------------------------")
print ("Write a Python program to replace last value of tuples in a list.")
# replace value of tuple 
l = [(10, 20, 40)]
print (l)
print([t[:-1] + (30,) for t in l])

print ("------------------------------------------- QUESTION - 27 ----------------------------------------------")
print ("Write a Python program to find the repeated items of a tuple.")
# count repete number 
num_list  = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(num_list)
count = num_list.count(4)
print(count)

print ("------------------------------------------- QUESTION - 28 ----------------------------------------------")
print ("Write a Python program to remove an empty tuple(s) from a list of tuples.")
# remove an empty tuple(s) from list 
A = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
B = [t for t in A if t]
print (A)
print (B)

print ("------------------------------------------- QUESTION - 29 ----------------------------------------------")
print ("Write a Python program to unzip a list of tuples into individual lists.")
#  unzip a list of tuple 
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))

print ("------------------------------------------- QUIESTION - 30 ---------------------------------------------")
print ("Write a Python program to convert a list of tuples into a dictionary.")
# Python code to convert into dictionary
def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di
name_list = [("Devang", 21), ("Avi", 20)]
dictionary = {}
print (Convert(name_list, dictionary))

menu4="""
Q.31) How will you create a dictionary using tuples in python?
ANS. 
     >>  To convert a tuple to dictionary in Python, use the dict() method. 
     >>  The dict() function takes a tuple of tuples as an argument and returns the dictionary. 
	 >>  Each tuple contains a key-value pair.
"""
print ("------------------------------------------- QUESTION - 32 ----------------------------------------------")
print ("Write a Python script to sort (ascending and descending) a dictionary by value.")
# ascending and descending 
import operator
A = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print('Original dictionary : ',A)
sorted_d = sorted(A.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(A.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

print ("------------------------------------------- QUESTION - 33 ----------------------------------------------")
print ("Write a Python script to concatenate following dictionaries to create a new one.")
# dictionaries create new one 
dic1={1:2, 3:4}
dic2={5:6, 7:8}
dic3 = {}
for B in (dic1, dic2): dic3.update(B)
print(dic3)

print ("------------------------------------------- QUESTION - 34 ----------------------------------------------")
print ("Write a Python script to check if a given key already exists in a dictionary.")
# check if a given key already exists in a dictionary 
C = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in C:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(2)
is_key_present(70)

menu4 = """
Q.35)	How Do You Traverse Through A Dictionary Object In Python?
ANS.
	>>	Dictionaries are one of the most important and useful data structures in Python. 
	>>	They can help you solve a wide variety of programming problems. 
	>>	This tutorial will take you on a deep dive into how to iterate through a dictionary in Python.

Q.36)	How Do You Check The Presence Of A Key In A Dictionary?
ANS.
	>>	Using has_key() method returns true if a given key is available in the dictionary, otherwise, it returns a false. 
	>>	With the Inbuilt method has_key(), use the if statement to check if the key is present in the dictionary or not. 
"""
print (menu4)

print ("------------------------------------------- QUESTION - 37 ----------------------------------------------")
print ("Write a Python script to print a dictionary where the keys are numbers between 1 and 15.")
# print dictionary, the keys are number between 1 to 15 .
C=dict()
for x in range(1,16):
    C[x]=x**1
print(C)

print ("------------------------------------------- QUESTION - 38 ----------------------------------------------")
print ("Write a Python program to check multiple keys exists in a dictionary")
# check multiple keys exists in a dictionaqry 
Candidate = {'name': 'Devang','class': 'BCA','roll_id': '2'}
print(Candidate.keys() >= {'class', 'name'})
print(Candidate.keys() >= {'name', 'Devang'})

print ("------------------------------------------- QUESTION - 39 ----------------------------------------------")
print ("Write a Python script to merge two Python dictionaries")
# merge two python dictionaries 
D1 = {'a': 100, 'b': 200}
D2 = {'c': 300, 'd': 200}
D = D1.copy()
D.update(D2)
print(D)

print ("------------------------------------------- QUESTION - 40 ----------------------------------------------")
print ("Write a Python program to map two lists into a dictionary")
# map two lists into a dictionary 
Keys = ['green', 'blue','red']
values = ['#008000', '#0000FF','#FF0000']
color= dict(zip(Keys, values))
print(color)

print ("------------------------------------------- QUESTION - 41 ----------------------------------------------")
print ("Write a Python program to combine two dictionary adding values for common keys.")
print ("d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}")
# combine two dictionary adding values for common keys 
from collections import Counter
E1 = {'a': 100, 'b': 200, 'c':300}
F1 = {'a': 300, 'b': 200, 'd':400}
G = Counter(E1) + Counter(F1)
print(G)

print ("------------------------------------------- QUESTION - 42 ----------------------------------------------")
print ("Write a Python program to print all unique values in a dictionary.")
# print all unique values in a dictionary
H = [{"0":"S001"}, {"1": "S002"}, {"2": "S001"}, {"3": "S005"}, {"4":"S005"}, {"5":"S009"},{"6":"S007"}]
print("Original List: ",H)
I = set( val for dic in H for val in dic.values())
print("Unique Values: ",I)

print ("------------------------------------------- QUESTION - 44 ----------------------------------------------")
print ("Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.")
print ("Sample data: {'1': ['a','b'], '2': ['c','d']}")
# display all combinations of letters,selecting each letter
import itertools      
J ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[J[k] for k in sorted(J.keys())]):
    print(''.join(combo))

print ("------------------------------------------- QUESTION - 45 ----------------------------------------------")
print ("Write a Python program to find the highest 3 values in a dictionary")
# finding 3 highest values in a Dictionary
from collections import Counter
K = {'A': 67, 'B': 23, 'C': 45,
		'D': 56, 'E': 12, 'F': 69}
L = Counter(K)
high = L.most_common(3)
print(K, "\n")
print("Dictionary with 3 highest values:")
for i in high:
	print(i[0]," :",i[1]," ")

print ("------------------------------------------- QUESTION - 46 ----------------------------------------------")
print ("Write a Python program to combine values in python list of dictionaries.")
print ("Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]")
# combine value in python list of dictionaries
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for M in item_list:
    result[M['item']] += M['amount']
print(result) 

print ("------------------------------------------- QUESTION - 47 ----------------------------------------------")
print ("Write a Python program to create a dictionary from a string.")
print ("Note: Track the count of the letters from the string.")
print ("Sample string: 'w3resource'")
# create a dictionary from a string 
from collections import defaultdict, Counter
N = 'w3resource' 
O = {}
for letter in N:
    O[letter] = O.get(letter, 0) + 1
print(O)

print ("------------------------------------------- QUESTION - 48 ----------------------------------------------")
print ("Write a Python function to calculate the factorial of a number (a nonnegative integer)")
# calculate the factorial of a number 
def factorial(P):
    if P == 0:
        return 1
    else:
        return P * factorial(P-1)
P=int(input("Input a number to compute the factiorial : "))
print(factorial(P))

print ("------------------------------------------- QUESTION - 49 ----------------------------------------------")
print ("Write a Python function to check whether a number is in a given range.")
# whether a number is in a given range 
def test_range(Q):
    if Q in range(1,7):
        print( " %s is in the range " %str(Q))
    else :
        print("The number is outside the given range.")
test_range(5)

print ("------------------------------------------- QUESTION - 50 ----------------------------------------------")
print ("Write a Python function to check whether a number is perfect or not.")
# check wheter a number is perfect or not 
def perfect_number(n):
    dum = 0
    for x in range(1, n):
        if n % x == 0:
            dum += x
    return dum == n
print(perfect_number(6))

print ("------------------------------------------- QUESTION - 51 ----------------------------------------------")
print ("Write a Python function that checks whether a passed string is palindrome or not")
# check wheter a passed string is palindrome or not 
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('dmd')) 

menu5 ="""
Q=43) Why Do You Use the Zip () Method in Python?
ANS.
	>> 	The zip() function returns a zip object, which is an iterator of tuples where the first item in 
		each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

Q=52) How Many Basic Types Of Functions Are Available In Python?
ANS.
	>>	There are three types of functions in Python:
		>>	Built-in functions, such as help() to ask for help, min() to get the 
			minimum value, print() to print an object to the terminal

Q=53)	How can you pick a random item from a list or tuple?
ANS.
	>>	The choice() method is used to return a random number from given sequence. The sequence can be a list or a tuple. 
		This returns a single value from available data that considers duplicate values in the sequence(list). 

Q=54) How can you pick a random item from a range?
ANS.
	>> Use a random.randrange() function to get a random integer number from the given exclusive range by specifying the increment.

Q=55) How can you get a random number in python?
ANS.
	>>	To generate random number in Python, randint() function is used. This function is defined in random module.

Q=56) How will you set the starting value in generating random numbers?
ANS.
	>>	The seed() method is used to initialize the random number generator.
	
	>>	The random number generator needs a number to start with (a seed value), to be able to generate a random number.

Q=57) How will you randomizes the items of a list in place?
ANS.
	>>	The shuffle() method randomizes the items of a list in place.
"""
print (menu5)

print ("------------------------------------------- QUESTION - 59 ----------------------------------------------")
print ("Write a Python program to convert degree to radian")
# convert degree to radian 
pi=22/7
degree = float(input("Input degrees: "))
radian = degree*(pi/180)
print(radian)

print ("------------------------------------------- QUESTION -60 -----------------------------------------------")
print ("Write a Python program to calculate the area of a trapezoid")
#  calculate the area of a trapezoid 
base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)

print ("------------------------------------------- QUESTION - 61 ----------------------------------------------")
print ("Write a Python program to calculate the area of a parallelogram")
#  calculate the area of a parallelogram 
base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)

print ("------------------------------------------- QUESTION - 62 ----------------------------------------------")
print ("Write a Python program to calculate surface volume and area of a cylinder")
# calculate surface volume and area of a cylinder 
pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)

print ("------------------------------------------- QUESTION - 63 ----------------------------------------------")
print ("Write a Python program to returns sum of all divisors of a number")
# returns sum of all divisors of a number 
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))

print ("------------------------------------------- QUESTION - 64 ----------------------------------------------")
print ("Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.")
from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))

print ("------------------------------------------- THANK YOU --------------------------------------------------")