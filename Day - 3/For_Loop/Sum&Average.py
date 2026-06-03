a = []
print("Enter 10 Numbers")
for i in range(10):
    num = int(input("Enter number"+str(i+1)+" :"))
    a.append(num)
sum = 0
for i in a:
    sum = sum+i
    avg = sum/10
print(sum)    
print(avg)
