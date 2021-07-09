#d1={}     ------------->CREATING A DICTIONARY
d2={"Rohan":"Burger","Abhinav":"Roti","Aparna":"Chapati","Priya":{"A":"B","C":"D"}}
#print(type(d1))
#print(d2["Rohan"])
#print(d2["Burger"])         ------>ERRORpr
#print(d2["Priya"])
#print(d2["Priya"]['C'])
d2["Abhi"]="Pizza"
print(d2)
#del d2["Abhi"]
#print(d2)
d2.update({"Ranju":"Momos"})
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
d2.popitem()
print(d2)
