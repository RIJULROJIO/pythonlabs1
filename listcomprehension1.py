n=int(input("Enter the number of elements:"))
list=[]
for i in range(0,n):
    lis=int(input("Enter the elements to the list:"))
    list.append(lis)
print("Positive numbers in the list",list, "are:")
list2=[]
for i in list:
    if i>=0:
        #print(i,end=" ")
        list2.append(i)
print(list2)

