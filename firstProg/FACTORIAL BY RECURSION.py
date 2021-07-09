""""-------FACTORIAL BY ITERATIVE APPROACH-------
f=1
n=int(input("ENTER THE NUMBER: "))
for i in range(1,n+1):
    f=f*i
print(f)"""

#-------FACTORIAL BY RECURSIVE APPROACH-------
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter the number: "))
print(fact(n))
