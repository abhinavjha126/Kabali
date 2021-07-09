a=int(input("Enter the Number: "))
for i in range(1,a+1):
    for j in range(2,i+1):
        print(" ",end=" ")
    for k in range(1,a-i+2):
        print("*",end=" ")
    print()