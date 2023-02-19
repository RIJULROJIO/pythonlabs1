n1=int(input("Enter the First number:"))
n2=int(input("Enter the Second number:"))
i=1
while(i<=n1 and i<=n2):

  if(n1%i==0 and n2%i==0):
   gcd=i
  i=i+1
print("GCD is",gcd)



