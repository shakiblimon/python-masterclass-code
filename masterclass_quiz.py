# Passing function as arguments #
#################################

def add(a,b):
    return a+b
def suare (c):
    return c*c

result = suare(add(2,3))

print(result)





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





#  List Comprehension
############################
list =[x**2 for x in  range(8) if x**2 % 2 == 0 ]
print( list)










