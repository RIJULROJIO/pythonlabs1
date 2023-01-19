import csv
 #open the csv file

with open('samp.csv','r') as file:
     # create a csv reader
     reader=csv.reader(file)

     # iterate over th e rows of the csv file
     for row in reader:
          # print the row as a list of strings
        print(row)

