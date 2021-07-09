import random
a=int(input("HOW MANY NAMES YOU WANT TO ENTER:"))
s=[]
for i in range(0,a):
    b=input(f"ENTER {i+1} NAME:")
    s.append(b)
t=[]
n=[]
for i in range(0,len(s)):
    c = s[i].split(" ")
    for j in range(0,len(c)):
        if j!=0:
           n.append(c[j])
        else:
           t.append(c[j])
print(t)
print(n)
f=1
while f<10:
       p = random.randint(0,(len(t)-1))
       q = random.randint(0,(len(n)-1))
       print("THE FUNNY NAME IS:",end="")
       print(f"{t[p]} {n[q]}")
       v=f"{t[p]} {n[q]}"
       for i in range(0,a):
           if v==s[i]:
             print("\t\t\tOHHHOOOO......CORRECT COMBINATION")
       f+=1
