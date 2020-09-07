with open("sports.txt" , "r") as robj:
    with open("Athletic.txt" , "w") as wobj:
        str = robj.readlines()
        for i in str:
            if "Athletics" in i:
                wobj.write(i + "\n")
        print("Operation Completed")