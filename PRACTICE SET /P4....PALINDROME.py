n = int(input("Enter the Number of Strings you want to Enter: "))

def palindrome(s):
    return str(s)==str(s)[::-1]

if __name__ == '__main__':
    for i in range(n):
        a = int(input(f"Enter the {i + 1} Number:"))
        while not palindrome(a):
            a += 1
            if palindrome(a):
                print(f"The Next Palindrome Number is: {a}")


