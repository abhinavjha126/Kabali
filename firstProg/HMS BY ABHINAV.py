print("------------HEALTH MANAGEMENT SYSTEM------------")
def getdate():
    import datetime
    return datetime.datetime.now()
Client_Name = {1: "ABHINAV", 2: "PRIYA", 3: "APARNA"}
Client_Activity = {1: "EXCERCISE", 2: "FOOD"}

try:
    print("Enter Client Number")
    for key, value in Client_Name.items():
        print(key, "for", value)
    ab1 = int(input())

    print("Press 1 for log")
    print("Press 2 for retrieve")
    op = int(input())

    if op == 1:
        print("Which Activity you want to enter:Plzzz tell!")
        for key, value in Client_Activity.items():
            print(key, "for", value)
        op = int(input())
        print("Selected Activity: ", Client_Activity[op])
        f = open(Client_Name[ab1] + "_" + Client_Activity[op] + ".txt", "a")
        k='Y'
        while(k !='N'):
            print("Enter", Client_Activity[op], "\n", end="")
            mytext = input()
            f.write("[" + str(getdate()) + "]:" + mytext + "\n")
            k = input("Add More ? Y/N:")
            continue
        print("----ITEMS SUCCESSFULLY ADDED----")
        f.close()
    elif op == 2:
        for key, value in Client_Activity.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_Name = int(input())
        print(Client_Name[log_Name], "-", Client_Activity[log_Name], "Report:", "\n", end="")
        f = open(Client_Name[ab1] + "_" + Client_Activity[log_Name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as  e:
    print(e)

