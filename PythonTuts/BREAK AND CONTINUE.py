"""i=0
while True:
    if i+1<5:
        i=i+1
        continue
    print(i,end=" ")
    if i==29:
        break
    i=i+1"""

while 1:
    a = int(input("Enter the Number: \n"))
    if a<=100:
        print("Try again")
        continue
    else:
        print("Congratualations you hava entered number Greater than 100")
        break