# a=input("Enter your name: ")
# b=input("Enter your salary ")
#
# if int(b)==0:
#     raise ZeroDivisionError("b can't be 0")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello {a}")

c=input("Enter your Name: ")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("This name is blocked")
    print("Exception Handled")

