__version__ = "1.0.0"
__author__ = "Shakib Limon"


#   List operations
###################################
manes = ['limon','shakib','ratul', 'linkon', 'adnan','shohag']
print(len(manes))
manes.insert(0,'cse')

print(manes)
print(manes[1:4])
print('shakib' in manes)

#   range function in list
######################################
number = list(range(5,20,2))
print(number)


#   Code reuse function
###############################
def names ():
    print('limon')
    print('shakib')
    print('shohag')
    print('niloy')
    print('linkon')
    print('hafiz')
names()


#       while Loop
#################################
c= 1
while c<=10:
    print(c)
    c+=2

#   Challenge -1
########################

list =['pizza','bargre','khichuri','luci','vat']
print(list[2])
list.append('ruti')
print(list)
list.insert(3,'tacos')
print(list)

#    task -1 challenge -2
#################################

for x in range(5):
    print('i am a programmer')

    #task -2
def square():
    for x in range (1,10):
        print(x*x)
square()

# Passing function as arguments #
#################################

def add(a,b):
    return a+b
def suare (c):
    return c*c

result = suare(add(2,3))

print(result)


## Twice Functional Program  ##
###############################
def add (x):
    return x+10

def twice(func, arg):
    return func (func(arg))

print(twice(add,10))


#          Module in python #
#############################

import random

for i in range (5):
    result= random.randint(1,6)
    print(result)

### BMI Calculator ####
#######################

def BMI(new_height,new_weight):
    bmi = new_weight/(pow(new_height,2))
    return  bmi
weight = float(input('Enter the weight in kgs: '))
height = float(input('Enter the height in meters: '))
result = BMI(height,weight)
print(BMI)

# Exception Handling with finally #
###################################

try:
    a=20
    b= 30
    print(a/b)
except ZeroDivisionError:
    print('Value is divided   by zero ')
finally:
    print('its done ')

##      File Handling
#################################

file  =  open("test.txt",'r')
content = file.read()
print(content)
file.close()


##  Dictionaries ##
###################
people = {"shakib":23,"Limon":25,"optime":30}
print(people["shakib"])

## Dictionaries Function

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
print(2 in  numbers)  ## to get the 2 no position item
print(numbers.get(5," key value not found")) ### if the value are not in the l ist

####    Tuples  ###
###################

### its similar to  list but  here we cant cahnge the item of list that store in .
fruits = 'apple', 'mango','peach'
print(fruits)
print(fruits[2])  ## index use as like as list


### List Slicing ##
######################

num = [1,20,30,40,60,80,90,100,130,150,170,190]

print(num[0:12]) # With start and end index

print(num[1:9:3]) # With interval point


#  List Comprehension
############################
list =[x**2 for x in  range(8) if x**2 % 2 == 0 ]
print( list)


#       Functional Python
#############################

    #   Lambdas
def square(x):
    return (x**3)
print(square(3))

result = (lambda x:x**3)(20)
print(result)

    #  Map in python

def add(x):
    return (x+2)

newlist=[10,20,40,50,70,100]

rst = list(map(add,newlist))
print(rst)
##print(list(map(add,newlist)))    ## Also can print like here

## Without define the function we can do it using lambdas

# rst = list(map( lambda x:x+2 , newlist))


    # Filters

newlist=[10,1,20,3,40,4,50,7,70,2,100,8]

result = list(filter(lambda x: x%2 ==0 ,newlist))
print(result)

    #   Generators
def function():
    counter = 0
    while counter <10:
        yield counter
        counter += 1
for x in function():
    print(x)


    #   Finding even number with generator
def even(x):
    for i  in range(x):
        if i %2 == 0 :
            yield i
print(list(even(20)))


#############################################
#       Object Oriented Python
#############################################
class Students:         #Craeting class
    def __init__(self,name,contact):     # Initaiting class propertices
        self.name= name
        self.contact = contact



    def getdate(self):
        print(' Raedy to Accept Data')
        self.name = input('Enter Name : ')
        self.contact = input('Enter Contact: ')

    def putdata(self):
        print('The name is  : '+self.name, '\nThis is  the contact: '+self.contact)

shakib = Students('blank',0)
shakib.getdate()
shakib.putdata()



