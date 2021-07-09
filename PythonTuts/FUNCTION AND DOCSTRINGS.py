""""-----------BUILT IN FUNCTION
a=9
b=5
c=sum((a,b))
print(c)
----------USER DEFINED FUNCTIONS
a=9
b=5
def func1():
    print("THE SUM OF NUMBERS IS: ",a+b)
def func2():
    avg=(a+b)/2
    return avg
#func1()
#print(func1())
func2()
#print(func2())"""
def avg(a,b):
    """This is a function to calculate average of 2 numbers"""
    avg=(a+b)/2
    return avg
print(avg.__doc__)