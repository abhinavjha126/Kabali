import re
# list1=re.findall(r'\w+@\w+\.\w+')
str="""Hello bro, my name is deepak tiwari and my email id is deepak@gmail.com,
     And I am learning programming on code with harry youtube channel and I have one more
     email:deepak@dt.com and some more email id:<dt123@codewithharry.com"""
a=re.compile(r"\w+@\S+\w")
matches=a.finditer(str)
j=1
for i in matches:
     s= f"{i}"
     file="email_extractor.txt"
     f=open(file,"a")
     print=f.writelines(f"E-MAIL {j}={i}\n")
     j+=1