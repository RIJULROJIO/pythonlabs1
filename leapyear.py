start_year=int(input("Enter the Starting year:" ))
final_year=int(input("Enter the Final year:"))
print("The list of leap years:")
for year in range(start_year,final_year):

 if(year%4 == 0) and (year%100!=0) or (year%400 == 0):
  print(year)
