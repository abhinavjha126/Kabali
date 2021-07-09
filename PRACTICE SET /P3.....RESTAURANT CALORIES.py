a=[]
n=int(input("Enter the Number of Calories Items you want to Add in list: "))
for i in range(n):
    b=int(input("Enter the Calories:"))
    a.append(b)
print(a)

def inbuilt():
    a.sort()
    print(f"The Sorted List by Inbulit Method: {a}")
def slicing():
    c=a[::-1]
    c.reverse()
    print(f"The Sorted List by Slicing Method: {c}")
def swapping():
    for i in a:
        if i<n/2:
           a[i],a[n-i-1]=a[n-i-1],a[i]
    print(f"The Sorted List by Swapping Method: {a}")

if __name__ == '__main__':
    inbuilt()
    slicing()
    swapping()
