def abhi():
    import time
    dict = "abhi jha priya jaya mohit aparna bateshwar ranju saurabh bir muskesh suresh and ji"
    time.sleep(4)

    while 1:
        text = (yield)
        if text in dict:
            print("TEXT IS IN THE DICTIONARY")
        else:
            print("TEXT IS NOT IN THE DICTIONARY")

s=abhi()
print("SEARCHING STARTED.........")
next(s)
s.send("priyaa")
print("FUNCTION ENDS")