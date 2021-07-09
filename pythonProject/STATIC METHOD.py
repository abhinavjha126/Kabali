class School:
    pass

    @staticmethod
    def a(string):
     print(f"THIS IS GOOD {string}")
     return 2

harry = School()
harry.name = "HARRY"
harry.salary = 45
harry.id = 2

print(School.a("MORNING"))

