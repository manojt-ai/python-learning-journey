a = int (input("A: "))
b = int (input("B: "))
Operation = input("add/sub/mul/div: ")
if(Operation =="add"):
    print(a+b)
elif(Operation =="sub"):
    print(a-b)
elif(Operation=="mul"):
    print(a*b)
elif(Operation=="div"):
    print(a/b)
else:
    print("Invalid Operation")
