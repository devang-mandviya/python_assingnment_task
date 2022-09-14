print ("--------------------------- QUESTION - 1-----------------------------")
print ("[Write a Python program to check if a number is positive, negative or zero.]")
# check number positive and nagetive 
psum = 0
nsum = 0 

num = float(input("Enater your number :"))
if num > 0 :
    print ("positive number ")
elif num == 0 :
    print ("zero")
else :
    print ("Nagetive number ")        

print("----------------------------- QUESTION - 2 --------------------------")
print("[Write a Python program to get the Factorial number of given number.]")
# find fectorial number 
from re import I

num = int(input("Enter a number :"))
factorial = 1 
if num < 0 :
    print ("factorial does not exist for negative number ")
elif num == 0 :
    print ("The factorial of 0 is 1")
else :
    for i in range (1,num + 1):
        factorial = factorial*i 
    print ("The factorial of",num,"is",factorial) 

print ("---------------------------- QUESTION - 3 ------------------------")    
print ("[Write a Python program to get the Fibonacci series of given range.]")
# fabonacci series of given range 
num = int(input("Enter your number :"))
x=0
y=1
z=0
while(z<=num):
    print (z)
    x=y
    y=z
    z=x+y

print ("--------------------------------------------------------------")      
menu="""
Q.4)  How memory is managed in Python?
ANS. 
     >> Memory management in Python involves a private heap containing all Python objects and data structures. 
     >> The management of this private heap is ensured internally by the Python memory manager.

Q.5)  What is the purpose continue statement in python?
ANS. 
     >> The continue statement in python returns the control to the beginning of the while loop.
     >> The continue statement rejects all the remaining statements in the current iteration 
        of the loop and moves the control back to the top of the loop.
     >> The continue statement can be used in both while and for loops.
"""
print (menu)
print ("-------------------------------- QUESTION- 6 -------------------------")
print ("[Write python program that swap two number with temp variable and without temp variable.]")
#swap two number with temp variable and without temp variable.
x = 5.4
y = 10.3
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x = x + y 
y = x - y 
x = x - y 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

print ("---------------------------- QUESTION - 7 ----------------------------")
print ("[Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.]")
# check number is even or odd 
num = int(input("Enter number :"))
if num %2 == 0:
    print ("This number is even number ")
else:
    print("This number is odd number ")    

print ("---------------------------- QUESTION - 8 ------------------------------")
print ("[Write a Python program to test whether a passed letter is a vowel or not.]") 
# check letter is a vowel or not
letter = input("Input a letter of the alphabet: ")

if letter  in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
	print("%s is a vowel." % letter)
elif letter  == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % letter) 

print ("---------------------------- QUESTION - 9 --------------------------------")
print ("[Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.]")
# sum of three given 
# if two values are equal sum will be zero
def sum_three(a, b, c):
    if a == b or b == c or a==c:
        sum = 0
    else:
        sum = a + b + c
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))

print ("---------------------------- QUESTION - 10 ----------------------------------")
print ("[Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.]")
# two integer equal 
# sum difference 5 
def number(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(number(7, 2))
print(number(3, 2))
print(number(12, 17))

print ("---------------------------- QUESTION - 11 ------------------------------------")
print ("[Write a python program to sum of the first n positive integers.]")
# sum of 1 n positive number 
n = int(input("Enter a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integer :", sum_num)

print ("---------------------------- QUESTION - 12 ---------------------------------")
print ("[Write a Python program to calculate the length of a string.]")
# calculate the length of a string.
str = input("Enter a string: ")
print("Length of the input string is:", len(str))

print ("---------------------------- QUESTION - 13 --------------------------------")
print ("[Write a Python program to count the number of characters (character frequency) in a string]")
# count of string charcter 
def username (str):
    name = {}
    for n in str:
        keys = name.keys()
        if n in keys:
            name[n] += 1
        else:
            name[n] = 1
    return name
print(username("tops technology"))

print ("--------------------------------------------------------------------------")
menu = """
Q.14)  What are negative indexes and why are they used?
ANS.   
     >> Python supports “indexing from the end”, that is, negative indexing.
     >> This means the last value of a sequence has an index of -1, the second last -2, and so on.
     >> You can use negative indexing as your advantage when you want to pick values from the end (right side) of an iterable.
"""
print (menu)
print ("--------------------------------- QUESTION - 15 ------------------------------")
print ("[Write a Python program to count occurrences of a substring in a string.]")
# count occurrences of a substring in a string
line = 'i am very cute boy. i am very smart '
print()
print(line.count("i"))
print()

print ("--------------------------------- QUESTION - 16 ---------------------------------")
print ("[Write a Python program to count the occurrences of each word in a given sentence]")
# count the all words in line 
def count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print(count("my dog name is mini ,my dog is very cute."))

print ("---------------------------------- QUESTION - 17 --------------------------------")
print ("[Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.]")
# take two string word and 
# first two letter swap 
def chars_mix_up(a, b):
  num1 = b[:2] + a[2:]
  num2 = a[:2] + b[2:]

  return num1 + ' ' + num2
print(chars_mix_up('gav', 'dejjar'))

print ("---------------------------------- QUESTION - 18 -----------------------------------")
print ("[Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.]")
# string already ends with 'ing' then add 'ly' 
# length should be at least 3
def string(str):
  length = len(str)

  if length > 2:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'

  return str
print(string('de'))
print(string('dev'))
print(string('playing'))

print ("---------------------------------- QUESTION - 19 ------------------------------------")
print ("[ Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.]")
# line is not replace good word 
# this program to replace word 
def not_poor(str):
  anot = str.find('not')
  bpoor = str.find('poor')

  if bpoor > anot and anot>0 and bpoor>0:
    str = str.replace(str[anot:(bpoor+4)], 'good')
    return str
  else:
    return str
print(not_poor('The study is not that poor!'))
print(not_poor('The study is poor!'))

print ("---------------------------------- QUESTION - 20 ----------------------------------")
print ("[Write a Python function that takes a list of words and returns the length of the longest one.]")
# find longest word 
def find_longest(words_list):
    l1 = []
    for n in words_list:
        l1.append((len(n), n))
    l1.sort()
    return l1[-1][0], l1[-1][1]
result = find_longest(["dev", "gajjar", "mandviya"])
print("Longest word: ",result[1])
print("Length of the longest word: ",result[0])

print ("---------------------------------- QUESTION - 21 -------------------------------------")
print ("[Write a Python function to reverses a string if its length is a multiple of 4.]")
# reverse word for multiple for 4 
name = input("Enter a name :")
if(len(name) %4 == 0):
    print(name[::-1])
else:
    print ("plese enter 4 letter word ")

print ("---------------------------------- QUESTION - 22 ----------------------------------------")
print ("[Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.]")
# first 2 and last 2 letter print only string 
def word(str):
  if len(str) < 2:
    return " "
  return str[0:2] + str[-2:]
print(word("devang"))

print ("---------------------------------- QUESTION - 23 ---------------------------------------")
print("[Write a Python function to insert a string in the middle of a string.]")
# middel string value insert 
def insert_sting_middle(str, word):
	return str[:1] + word + str[1:]

print(insert_sting_middle('<>', 'Devang'))
print(insert_sting_middle('//', 'Gajjar'))
print(insert_sting_middle('{}', 'python'))
