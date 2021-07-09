class Employee:
    def __init__(self,f1,l1):
        self.fname=f1
        self.lname=l1
    @property
    def email(self):
        return f"MY EMAIL IS {self.fname}.{self.lname}126@gmail.com"

    # @email.setter
    # def email(self,string):
    #     name=string.split("@")[0]
    #     self.fname=name.split(".")[0]
    #     self.lname=name.split(".")[1]
harry=Employee("abhi","jha")
# harry.email="harry.potter@gmail.com"
# print(harry.fname)
# print(harry.email)
print(type(harry))
print(id(harry))
print(dir(harry))
import inspect
print(inspect.getmembers(harry))
