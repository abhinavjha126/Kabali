"""def fun1(normal1,*args1,**kwargs1):
    print("I AM NORMAL:")
    print("\t\t",normal1)
    print("I AM ARGS: ")
    for item in args1:
        print("\t\t",item)
    print("I AM KWARGS: ")
    for key,value in kwargs1.items():
        print("\t\t",f"{key} is for {value}")
normal="My name is Abhinav"
args=["Abhinav","Rohan","Priya"]
kwargs={"1":"Abhinav","2":"Sunil","3":'Kavita'}
fun1(normal,*args,**kwargs)"""
kwargs={1:"Abhinav",2:"Sunil",3:'Kavita'}
print(type(kwargs))
for a,b in kwargs.items():
 print(a,b)