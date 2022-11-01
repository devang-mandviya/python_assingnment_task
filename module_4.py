menu1 = """
Q.1) What is File function in python? What is keywords to create and write file.
ANS.
    >>  Python has a built-in open() function to open a file. This function returns a file object, also called a handle, 
        as it is used to read or modify the file accordingly.
"""
print (menu1)

print ("------------------------------------------- Question - 2 -----------------------------------------------")
print ("Write a Python program to read an entire text file.")
menu2="""
#  read an entire text file 
def file_read(fname):
        txt = open(fname)
        print(txt.read())
file_read('test.txt')
"""
print (menu2)

print ("------------------------------------------- Question - 3 -----------------------------------------------")
print ("Write a Python program to append text to a file and display the text.")
# append text to a file and display the text
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Devang \n")
                myfile.write("Mandviya ")
        txt = open(fname)
        print(txt.read())
file_read('abc.txt')

print ("------------------------------------------- Question - 4 -----------------------------------------------")
print ("Write a Python program to read first n lines of a file.")
menu3="""
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as myfile:
                for line in islice(myfile, nlines):
                        print(line)
file_read_from_head('test.txt',2)
"""
print (menu3)

print ("------------------------------------------- Question - 5------------------------------------------------")
print ("Write a Python program to read last n lines of a file.")
menu4="""
def LastNlines(fname, N):
	with open(fname) as file:
		for line in (file.readlines() [-N:]):
			print(line, end ='')
if __name__ == '__main__':
	fname = 'File1.txt'
	N = 3
	try:
		LastNlines(fname, N)
	except:
		print('File not found')
"""
print (menu4)

print ("------------------------------------------- Question - 6 -----------------------------------------------")
print ("Write a Python program to read a file line by line and store it into a list")
menu5="""
with open("data_file.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)
"""
print (menu5)

print ("------------------------------------------- Question - 7 -----------------------------------------------")
print ("Write a Python program to read a file line by line store it into a variable.")
menu6="""
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')
"""
print (menu6)

print ("------------------------------------------- Question - 8 -----------------------------------------------")
print ("Write a python program to find the longest words.")
menu7="""
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))
"""
print (menu7)

print ("------------------------------------------- Question - 9 -----------------------------------------------")
print ("Write a Python program to count the number of lines in a text file.")
menu8="""
with open(r"myfile.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)
"""
print (menu8)

print ("------------------------------------------- Question - 10 ----------------------------------------------")
print ("Write a Python program to count the frequency of words in a file.")
menu9="""
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
"""
print (menu9)

print ("------------------------------------------- Question - 11 ----------------------------------------------")
print ("Write a Python program to write a list to a file.")
menu10="""
f = open('gfg.txt', 'r')
print(f.read())
f.close()
"""
print (menu10)

print ("------------------------------------------- Question - 12 ----------------------------------------------")
print ("Write a Python program to copy the contents of a file to another file.")
menu11="""
from shutil import copyfile
copyfile('test.py', 'abc.py')
"""
print (menu11)

menu12 ="""
Q.13) Explain Exception handling? What is an Error in Python?
ANS.
    >>  An Exception is an error that happens during the execution of a program. Whenever there is an error, 
        Python generates an exception that could be handled. It basically prevents the program from getting crashed.

Q.14)How many except statements can a try-except block have? Name Some built-in exception classes:
ANS.
    >>  In our previous lesson on Errors and Exceptions in Python. Now, we are going to explore Python Exception Handling.

    >>  Here, we will discuss try/except blocks, finally block, and raise block. Along with this, we will learn how to define your own python exception.

Q.15) when will the else part of try-except-else be executed ?
ANS.
    >> The else part is executed when no exception occurs.

Q.16) Can one block of except statements handle multiple exception?
ANS.
    >>  In Python, try-except blocks can be used to catch and respond to one or multiple exceptions.
         In cases where a process raises more than one possible exception, they can all be handled using a single except clause.

Q.17) When is the finally block executed?
ANS.
    >>  The finally block will be executed no matter if the try block raises an error or not.

    >>  This can be useful to close objects and clean up resources.

Q.18) What happens when „1‟== 1 is executed?
ANS.
    >>  	we get a false „1‟== 1 is executed

Q.19) How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
ANS.
"""
print (menu12)
# import module sys to get the type of exception
import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

print ("------------------------------------------- Question - 20 ----------------------------------------------")
print ("Write python program that user to enter only odd numbers, else will raise an exception.")
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

menu13="""
Q.21)What are oops concepts? Is multiple inheritance supported in java
ANS.
    >>  Multiple Inheritance is a feature of an object-oriented concept, where a class can inherit properties of more than one parent class.

    >>  The problem occurs when there exist methods with the same signature in both the superclasses and subclass.

Q.22)How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
ANS.
    >>  Almost everything in Python is an object, with its properties and methods.

    >>  A Class is like an object constructor, or a "blueprint" for creating objects.

    >>  EXAMPLE
                class MyClass:
                x = 5      
"""
print (menu13)

print ("------------------------------------------- QUestion 23 ------------------------------------------------")
print ("Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle")
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

print ("------------------------------------------- Question - 24 ----------------------------------------------")
print ("Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle")
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())

menu14="""
Q.25) Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?
ANS.
    >>  Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance in Python:

    >>  Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance

    >>  EXAMPLE OUTPUT -->
"""
print (menu14)
# single inheritance
class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child(Parent):
	def func2(self):
		print("This function is in child class.")
object = Child()
object.func1()
object.func2()

menu15="""
Q.26) What is Instantiation in terms of OOP terminology?
ANS. 
    >>  Instantiate (a verb) and instantiation (the noun) in computer science refer to the creation of an object 
        (or an “instance” of a given class) in an object-oriented programming (OOP) language.

    >>  Referencing a class declaration, an instantiated object is named and created, in memory or on disk.

Q.27) What is used to check whether an object o is an instance of class A?
ANS.
    >>  The isinstance() function checks if the object (first argument) is an instance or subclass of the class info class (second argument).

Q.28)  What relationship is appropriate for Course and Faculty?
ANS. 
    >>  association relationship is appropriate for Course and Faculty 

Q.29) What relationship is appropriate for Student and Person?
ANS.
    >>  association relationship is appropriate for Student and Person.
"""
print (menu15)