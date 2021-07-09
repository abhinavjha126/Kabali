n = int(input("Enter the Number of Strings you want to Enter: "))

def palindrome(s):
    return str(s) == str(s)[::-1]

if __name__ == '__main__':
    print("Enter the Numbers: ")
    s = []
    for i in range(n):
        a = int(input())
        s.append(a)
    print(s)
    for i in range(len(s)):
        b=s[i]
        if b > 10:
            while not palindrome(b):
                b=b+1
                if palindrome(b):
                    s[i]=b
            b=0
        else:
            s[i] = s[i]
    print(f"The Sorted List is: {s}")