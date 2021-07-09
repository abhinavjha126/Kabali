class School:
    no_of_leaves = 8
    def __init__(self,a,b,c):
        self.name=a
        self.id=b
        self.role=c

harry=School("Abhi",2,"Student")
print(harry.id)