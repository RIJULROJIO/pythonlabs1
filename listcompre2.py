n=int(input("Enter the number of elements:"))
list=[]
for i in range(0,n):
    lis=int(input("Enter the elements to the list:"))
    list.append(lis)
print("Square of the  numbers in the list",list, "are:")
list2=[]
for i in list:
   print(i*i)
   list2.append(i*i)