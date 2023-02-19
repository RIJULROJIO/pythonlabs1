str=input("Enter the string:")
b=str[0]
for i in str:
    if(str[0]==i):
        a=str.replace(i,'$')
print(b+a[1:])
