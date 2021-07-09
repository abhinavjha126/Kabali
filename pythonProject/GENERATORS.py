# dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2",]}
# print(dresses)
# print(type(dresses))
a = []
b = int(input("ENTER THE NUMBER OF ITEMS YOU WANT TO INCLUDE IN LIST: "))
c = 0
print("ENTER THE NUMBERS: ")
while c < b:
    d = int(input())
    a.append(d)
    c = c + 1
print(a)
print("Enter 1 for List Comprehension")
print("Enter 2 for Dictionary Comprehension")
print("Enter 3 for Set Comprehension\n")
i = int(input("PLEASE ENTER: "))
if i == 1:
    lst1 = [i for i in a]
    print(lst1)
    print(type(lst1))
elif i == 2:
    lst2 = {i: f"item{i}" for i in a}
    print(lst2)
    print(type(lst2))
elif i == 3:
    lst3 = {i for i in a}
    print(lst3)
    print(type(lst3))
else:
    print("WRONG INPUT....ENTER AGAIN")
