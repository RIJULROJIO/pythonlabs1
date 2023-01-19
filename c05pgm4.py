import csv
# specify the column indices that you want to read
# eg. column 0 is the first column,column 1 is the second column etc..
columns_to_read=[0,2]
# open the csv file and read the contents
with open('samp.csv','r') as f:
   clmn_reader= csv.reader(f)

   #iterate over the rows of the csv file

   for row in clmn_reader:
     # print the contents pf the specified columns
     print([row[i] for i in columns_to_read])
