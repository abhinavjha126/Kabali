# class Employee:
#     no_of_objects=8
#     def __init__(self,a,b,c):
#        self.name=a
#        self.salary=b
#        self.Id=c
#     def __truediv__(self, other):
#         return other.salary/ self.salary
#     def __add__(self, other):
#        return other.salary+self.salary
#
# harry=Employee("HARRY",3000,2)
# abhi=Employee("ABHINAV",5000,5)
# print(harry=abhi)
from abc import ABC,abstractmethod