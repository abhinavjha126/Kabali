# import time
# initial=time.time()
# print(initial)
# i=0
# while i<45:
#     print(i)
#     i+=1
# a=time.time()
# print(a-initial)
# for i in range (45):
#     print(i)
# print(time.time()-a)
import time
# import math
# h=0
# while h<5:
#     print("ABHINAV")
#     time.sleep(math.floor(1.1))
#     h+=1
localtime=time.asctime(time.localtime(time.time()))
print(localtime)