class School:
    no_of_leaves = 8
    def printdetails(a,b):
        return (f"Name is {a.name}")

harry = School()
rohan = School()

harry.name = "HARRY"
harry.salary = 45, 000
harry.id = 2

rohan.name = "ROHAN"
rohan.salary = 25000
rohan.id = 1

print(rohan.printdetails(1))
# School.no_of_leaves = 12
#
# print(rohan.__dict__)
# rohan.no_of_leaves = 12
# print(rohan.__dict__)
# print(rohan.no_of_leaves)
