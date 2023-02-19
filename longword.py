n=int(input("Enter the number of elements:"))
list=[]
for i in range(0,n):
    lis=input("Enter the elements to the list:")
    list.append(lis)
print(list)
max=len(list[0])
temp=len(list[0])
for i in list:
    if(len(i)>max):
               max=len(i)
               temp=len(i)
print("The length of the longest word is:")
print(temp)

