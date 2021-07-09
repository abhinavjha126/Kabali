# def add(a,b):
#     return a+b
# add=lambda a,b:a+b
# print(add(4,7))
a=[[1,2,5],[3,5,1],[7,1,3]]
a.sort(key=lambda x:x[2])
print(a)