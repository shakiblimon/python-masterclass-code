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