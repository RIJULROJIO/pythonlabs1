fruits={'apple':3,'grapes':29,'pineapple':65,'bananna':11}
print("the dictionary is {}\n".format(fruits))
l=list(fruits.items())
l.sort()
print('ascending order is:',l)
l=list(fruits.items())
l.sort(reverse=True)
print('descending order is:',l)