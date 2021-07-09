import random

print("\t\t\t\t\t\t\t\t-------------WELCOME TO THE GAME OF STONE,PAPER AND SCISSOR-------------")
print("\t\t\t\t\t\t\t\t\t\t\t\t\tTHIS IS A SERIES OF 5 MATCHES")
print("Enter \n 0 for Stone \n 1 for Paper \n 2 for Scissor")
count = 0
p = 0
c = 0

while count < 5:
    a = random.randint(0, 2)
    b = int(input("Enter the Number:"))
    if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
        print(f"COMPUTER CHOOSED {a}")
        print("COMPUTER WINS")
        c = c + 1
        count = count + 1
        print(f"GAMES LEFT = {5 - count}")
        if c > p:
            print(f"YOU ARE LAGGING BY {p}-{c}\n")
        elif c < p:
            print(f"YOR ARE AHEAD BY {p}-{c}\n")
        else:
            print(f"EQUAL SCORES {p}-{c}\n")
    elif (b == 0 and a == 2) or (b == 1 and a == 0) or (b == 2 and a == 1):
        print(f"COMPUTER CHOOSED {a}")
        print("PLAYER WINS")
        count = count + 1
        p = p + 1
        print(f"GAMES LEFT = {5 - count}")
        if c > p:
            print(f"YOU ARE LAGGING BY {p}-{c}\n")
        elif c < p:
            print(f"YOR ARE AHEAD BY {p}-{c}\n")
        else:
            print(f"EQUAL SCORES {p}-{c}\n")
    elif (a == 0 and b == 0) or (a == 1 and b == 1) or (a == 2 and b == 2):
        print(f"COMPUTER CHOOSED {a}")
        print("IT'S A DRAW")
        count = count + 1
        print(f"GAMES LEFT = {5 - count}")
        if c > p:
            print(f"YOU ARE LAGGING BY {p}-{c}\n")
        elif c < p:
            print(f"YOR ARE AHEAD BY {p}-{c}\n")
        else:
            print(f"EQUAL SCORES {p}-{c}\n")
    else:
        print("WRONG INPUT...PLEASE ENTER EITHER 0,1 OR 2")
        print(f"GAMES LEFT = {5 - count}")
        if c > p:
            print(f"YOU ARE LAGGING BY {p}-{c}\n")
        elif c < p:
            print(f"YOR ARE AHEAD BY {p}-{c}\n")
        else:
            print(f"EQUAL SCORES {p}-{c}\n")
    if count == 5 and c == p:
        print(f"SCORE TIED BY {c}-{p}..........................PLAY KNOCKOUT GAME\n")
        while c is p:
            a = random.randint(0, 2)
            print(f"GAMES LEFT = 1")
            b = int(input("Enter the Number:"))
            if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
                print(f"COMPUTER CHOOSED {a}")
                print("COMPUTER WINS")
                c = c + 1
                count = count + 1
                if c > p:
                    print(f"YOU ARE LAGGING BY {p}-{c}\n")
                elif c < p:
                    print(f"YOR ARE AHEAD BY {p}-{c}\n")
                else:
                    print(f"EQUAL SCORES {p}-{c}\n")
            elif (b == 0 and a == 2) or (b == 1 and a == 0) or (b == 2 and a == 1):
                print(f"COMPUTER CHOOSED {a}")
                print("PLAYER WINS")
                count = count + 1
                p = p + 1
                if c > p:
                    print(f"YOU ARE LAGGING BY {p}-{c}\n")
                elif c < p:
                    print(f"YOR ARE AHEAD BY {p}-{c}\n")
                else:
                    print(f"EQUAL SCORES {p}-{c}\n")
            elif (a == 0 and b == 0) or (a == 1 and b == 1) or (a == 2 and b == 2):
                print(f"COMPUTER CHOOSED {a}")
                print("IT'S A DRAW")
                p=p+1
                c=c+1
                count = count + 1
                if c > p:
                    print(f"YOU ARE LAGGING BY {p}-{c}\n")
                elif c < p:
                    print(f"YOR ARE AHEAD BY {p}-{c}\n")
                else:
                    print(f"EQUAL SCORES {p}-{c}\n")
            else:
                print("WRONG INPUT...PLEASE ENTER EITHER 0,1 OR 2")
                if c > p:
                    print(f"YOU ARE LAGGING BY {p}-{c}\n")
                elif c < p:
                    print(f"YOR ARE AHEAD BY {p}-{c}\n")
                else:
                    print(f"EQUAL SCORES {p}-{c}\n")
if c > p:
    print("OOPS!!!!YOU LOOSE....COMPUTER WINS")
    print(f"YOU LOOSE BY {p}-{c}")
elif p > c:
    print("HURRAY.....YOU WON")
    print(f"YOY WON BY {p}-{c}")
else:
    print("SERIES DRAWN")
    print(f"EQUAL SCORE {p}-{c}")
