listSeveral = [
    1, 2, 3, 4, 5, 
    6, 7, 8, 9, 10,
    'A', 'B', 'C', 'D', 'E'
]
# Python can save different data type

# INDEXING 
print(listSeveral[0])  # access first items
print(listSeveral[-1]) # access last items

# SLICING
print(listSeveral[0:-1]) # access first items to last items
print(listSeveral[:15])  # access first index to index 15
print(listSeveral[10:])  # access index 10 to last index
print(listSeveral[-5:])  # access 5 last index

# CHANGING LIST
listSeveral[14] = "H"
listSeveral[10:] = ["F", "G", "H", "I", "J"]
print(listSeveral[0:])

# LIST FUNCTION
print(len(listSeveral)) # how many items on list
# print(sorted(listSeveral)) // this will be occur an error cause can't ordered different data type
print(sum(listSeveral[0 : 10])) # function that sum a number
print(min(listSeveral[0 : 10])) # function that show the lowest number
print(max(listSeveral[0 : 10])) # function that show the biggest number

# LIST METHODS
listSeveral.append("F") # add F in the end of list
listSeveral.pop()       # will delete the last items from list

# SEARCHING LIST
print(listSeveral.index('H')) # show what index is H in list
print("H" in listSeveral)     # check H on list and throw true or false







