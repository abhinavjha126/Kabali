a=int(input("Enter the Number of Apples Harry has got: "))
b=int(input("Enter the Minimum Range Value: "))
c=int(input("Enter the Maximum Range Value: "))
if b==c:
    raise Exception ("Range is not valid.......It's Invalid")
print(f"Range is: {[b,c]}")
if b<c:
    for i in range(b,c+1):
        if a%i==0:
            print(f"{i} Apples can be Distributed")
else:
    print("Input is Valid....Please Check ")