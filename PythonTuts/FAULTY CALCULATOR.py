print("ENTER THE FIRST NUMBER:",end="")
a=int(input())
print("ENTER THE OPERAND AMONG (+,-,*,/) :",end="")
b=input()
print("ENTER THE SECOND NUMBER:",end="")
c=int(input())
if b=='+':
    if a==56 and c==9:
        print(77)
    else:
        print(a+c)
if b=='-':
    print(a-c)
if b == '*':
    if a==45 and c==3:
        print(555)
    else:
        print(a*c)
if b=='/':
    if a==56 and c==6:
        print(4)
    else:
        print(a/c)


