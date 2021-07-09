n=19
count=0
print("---------WELCOME TO THR GAME OF GUESSES---------")
print("Remember you just have 4 attempts to clear this game")
print("Guess the number between 1 to 50:",end=" ")
while count<4 :
    if count>0:
        print("Enter the Number: ",end="")
    a=int(input())
    if a>50:
        print("Invalid input!.....Please Enter the Number between 1 and 50")
    if a>n and count<4 and a>=1 and a<50 :
        print("Number is greater")
        count=count+1
        print("Number of guesses left :",4-count)
        if count == 4:
            print("OOP's!! You failed to clear the game")
            print("The correct Number was: ", n)
        continue
    if a<n and count<4 and a>=1 and a<50:
        print("Number is smaller")
        count=count+1
        print("Number of guesses left :", 4-count)
        if count == 4:
            print("OOP's!! You failed to clear the game")
            print("The correct Number was: ", n)
        continue
    if a==n :
        print("Congratulations you have guessed the number right")
        count=count+1
        print("You guessed the number in",count,"attempts")
        print("Here is you winning gift--------IPHONE--------Go and enjoy!!!!")
        break


