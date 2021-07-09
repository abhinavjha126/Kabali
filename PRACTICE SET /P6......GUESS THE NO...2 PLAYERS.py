import random
n=random.randint(1,100)
while n>0 and n<101:
    a=int(input("PLAYERS A TURN....ENTER YOUR NUMBER: "))
    if a<n:
        print("NUMBER IS SMALLER")
    elif a>n:
        print("NUMBER IS GREATER")
    elif a==n:
        print("HURRAYYY.............PLAYER A WINS!!!!!")
        break

    b = int(input("PLAYERS B TURN....ENTER YOUR NUMBER: "))
    if b<n:
        print("NUMBER IS SMALLER")
    elif b>n:
        print("NUMBER IS GREATER")
    elif b==n:
        print("HURRAYYY.............PLAYER B WINS!!!!!")
        break
