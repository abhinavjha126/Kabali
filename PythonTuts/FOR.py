"""list1=[["ABHI",1],["PRIYA",5],["APARNA",7],["RANJU",2]]
dict1=dict(list1)
print(dict1)
#for a,b in dict1.items():
 #print(a,b)
for a in dict1:
     print(a)"""
list1=["ABHI","2","**",9,56,86,678,"AB9","9ABHI","+",int,float]
for a in list1:
    if str(a).isalnum():
        print(a)