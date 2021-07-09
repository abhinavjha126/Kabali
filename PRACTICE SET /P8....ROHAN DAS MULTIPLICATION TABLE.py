def rohan_Multiplication(n):
    m=[]
    for i in range(1,11):
        if i==8:
            m.append(n*i-2)
        else:
            m.append(n*i)
    return m
def is_correct(n):
    s=[]
    for i in range(1,11):
            s.append(n*i)
    return s
if __name__ == '__main__':
    a=int(input("ENTER THE NUMBER: "))
    print(rohan_Multiplication(a))
    g=rohan_Multiplication(a)
    print(is_correct(a))
    h=is_correct(a)
    o=[]
    for i in range(1,11):
        if g[i]==h[i]:
            o.append(g[i])
        else:
            print(f"ROHAN FUNCTION IS WRONG AT INDEX: {i}")
            break

