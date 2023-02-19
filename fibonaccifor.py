n=int(input("Enter the limit:"))
n1=0
n2=1
print("Fibonacci series:\n",n1, "\n",n2,"\n", end="")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end="\n")
print()



