#       Calculating the interest
####################################
p = int(input('Enter Value of p : '))
n = int(input('Enter Value of n : '))
r = int(input('Enter Value of r : '))

si = (p*n*r)/100

print("Interest is : ",si)


#       If statement
###################################
age = int(input("Enter the  age : "))
if age >= 18:
    print("you are adult")
else:
    print("you are not adult")


marks = int(input("Enter the marks : "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B ")
else:
    print("Grade D")

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

#   Loop with list
###############################
names = ['limon','ratul','mostak', 'shakib', 'linkon','niloy']
for x in names:
    print(x)

#   Boolean Logic
##############################

username = 'user'
password = 'admin123'

if username == 'admin' or password == 'admin123' :
    print('Welcome to this site ')
else:
    print(' invalid user')


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


