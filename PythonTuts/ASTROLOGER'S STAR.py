n=int(input("Enter the Number: "))
b=int(input("Enter either 1 or 0: "))
if(bool(b)==True):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
if(bool(b)==False):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*",end=" ")
        print()