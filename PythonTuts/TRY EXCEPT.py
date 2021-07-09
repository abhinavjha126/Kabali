a=input("Enter the First Number: ")
b=input("Enter the Second Number: ")
try:
    print("The sum of two numbers is: ",int(a)+int(b))
except Exception as e:
    print(e)
    print("THE PROGRAM ENDS HERE")