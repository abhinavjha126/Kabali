i=input("ENTER YOUR AGE/YEAR OF BIRTH:")
if (len(i)==1 or len(i)==2 or len(i)==3) and int(i)<0:
    raise Exception("AGE CANNOT BE NEGATIVE....PLZ ENTER VALID AGE")
if int(i)>2021:
    raise Exception("TELLING LIE...............YOU ARE NOT YET BORN")
if len(i)==1 or len(i)==2 or len(i)==3:
    a=100-int(i)
    print(f"YOU WILL GET 100 YEARS OLD IN: {2021+a}")
else:
    print(f"YOU WILL GET 100 YEARS OLD IN: {int(i)+100}")

print("DO YOU WANT TO KNOW YOUR AGE IN SOME PARTICULAR YEAR??????????")
print("PRESS Y/y FOR YES")
print("PRESS N/n FOR NO")
s=input()
if s=="Y" or s=="y":
     b=int(input("ENTER THE YEAR IN WHICH YOU WANT TO KNOW YOUR AGE: "))
     c=int(input("ENTER YOUR YEAR OF BIRTH: "))
     print(f"YOUR AGE WILL BE: {b-c}")
elif s=="N" or s=="n":
     "break"
else:
    print("INVALID INPUT")

# i=0
# while (True):
#     print(i+1,end=" ")
#     if(i==6):
#         break
#     i=i+1