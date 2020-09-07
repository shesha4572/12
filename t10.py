with open("story.txt" , "r") as f:
    str = f.read()
    words = len(str.split())
    jack = 0
    vowels = 0
    w_space = 0
    for i in str:
        if i.lower() in ("a" , "e" , "i" , "o" , "u"):
            vowels += 1
        elif i.isspace():
            w_space += 1
    for j in str.split():
        if j == "Jack":
            jack += 1
