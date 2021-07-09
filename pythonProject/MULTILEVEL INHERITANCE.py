class Electronic_gadget:
    def __init__(self, a):
        print(f"ABHI TIME HUA HAIN  {a} ")


class Pocket_Gadget(Electronic_gadget):
    def __init__(self,a):
            print(f"ABHI TIME YE HUA HAIN BEEEEEEEEEEE {a}")
    def __init__(self, a, b):
        print(f"ABHI TIME YE HUA HAIN BE {a} {b}")


class Phone(Pocket_Gadget):
    pass

a = Electronic_gadget(1)
b = Pocket_Gadget(1,2)
c = Phone(1)

print(c)
