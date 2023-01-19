                                             # program1
# using readLines()

open_file=open('demo.txt','r')
File_Lines=open_file.readlines()

print("\nFile Content: ")

print(File_Lines)

# by using strip

print("\n File content after removing newline character:")

File_Lines=[X.strip() for X in File_Lines]
print([X.strip() for X in File_Lines])

open_file.close()


