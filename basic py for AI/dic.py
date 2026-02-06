# Dictionary
# Dictionaries are used to store data values in key:value pairs.

thisCar = {
    "brand" : "bmw",
    "color" : "Black",
    "engine" : "V3"
}
# print(thisCar["brand"])

# Accessing Items
x = thisCar["brand"] 
x = thisCar.get("brand") # this also will throw the same result

# get items 
x = thisCar.items()
thisCar["engine"] = "V5"
thisCar["Country"] = "Europe"

# check if an key is exist 
if "brand" in thisCar :
    print("key is exist in dictionary")

# update and change an dictionary
biodata = {
    "nama" : "ahmadhakimitsnaini",
    "umur" : 20,
    "universitas" : "politeknik negeri madiun"
}

biodata.update({"universitas" : "Politeknik Negeri Madiun"})
biodata["nama"] = "Ahmad Hakim Itsnaini"

# add items
biodata["job"] = "Data Science"

# remove items
biodata.pop("job")
biodata.update({"job" : "Data Science"})
# biodata.popitem() # this will delete last items from dictionary 
del biodata["job"]
# del biodata # this will delete that biodata


# loop dictionary
for x, y in biodata.items() : 
    print(x , y)






