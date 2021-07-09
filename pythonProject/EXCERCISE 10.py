import pickle
import requests
# import bz2
# url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# req=requests.get(url).text
# spl=req.splitlines()
# a=[i for i in spl]
# file="exc.pkl"
# fileobj=open(file,"wb")
# sfile=bz2.BZ2File(fileobj,"wb")
# pickle.dump(a,fileobj)
# fileobj.close()

file="exc.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)

