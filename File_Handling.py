f = open("test.txt")
print("Before reading : " , f.tell())
s = f.read()
print("After reading : " , f.tell())
f.seek(0)
print("From beginning again : " , f.tell())
s = f.read(4)
print("First 4 bytes are : " , s)
print(f.tell())
s = f.read(3)
print("next 3 bytes : " , s)
print(f.tell())
f.close()