#-------------------------MAP-------------------------
#lis=["3","5","4","9"]
# for i in range(len(lis)):
#  print(int(lis[i])+5)
# for i in lis:
#  a=int(i)+5
#  print(a+5)
# lis=list(map(int,lis))
# print(lis)
#-------------------------MAP-------------------------
# lis=[1,4,2,7,8,9]
# gr_than_5=list(filter(lambda x:x>5,lis))
# print(gr_than_5)
#-------------------------REDUCE-------------------------
from functools import reduce
lis=[1,2,8,4,5]
n=reduce(lambda  x,y:x+y,lis)
print(n)
