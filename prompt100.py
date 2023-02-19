list=[]
n=int(input("Enter the limit:"))
for i in range(n):
    value=int(input("Enter the number:"))
    if value>100:
        value="over"
    list.append(value)
print(list)
