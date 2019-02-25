__version__ = "1.0.0"
__author__ = "Shakib Limon"


#       If statement
###################################
age = int(input("Enter the  age : "))
if age >= 18:
    print("you are adult")
else:
    print("you are not adult")

'''
        Grade Calculation
'''
marks = int(input("Enter the marks : "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B ")
else:
    print("Grade D")
