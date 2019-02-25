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
