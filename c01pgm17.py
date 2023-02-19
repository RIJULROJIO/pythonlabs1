def Merge(dict1,dict2):
    return (dict2.update(dict1))
dict1={'rijul':10,'alan':8}
print("the dictionary is",dict1)
dict2={'dustin':7,'jon':1}
print("the dictionary 2 is",dict2)
Merge(dict1,dict2)
print("after merging ")
print(dict2)