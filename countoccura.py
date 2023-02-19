list=[]
n=int(input("Enter the limit of the List:"))
print("Enter the first names:")
for i in range(0,n):
    elem=input()
    list.append(elem)
print(list)
count=0
for i in list:
    for j in i:
        if(j=='a' or j=="A"):
            count=count+1
print("The number of 'a' in the list are:",count)

