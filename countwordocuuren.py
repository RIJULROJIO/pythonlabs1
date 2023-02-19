str=input("Enter the string:")

count=0
word=input("Count of which word in the string:")
sp=str.split(" ")
for i in sp:
   if(i==word):
     count=count+1
print(count)
