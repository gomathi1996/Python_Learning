# Key, value pair
# key should be unique and it can be any type

threewordToFull = {
    0: "January",
    "FEB": "Febuary",
    "MAR": "March"
}

print(threewordToFull[0])
print(threewordToFull["FEB"])
print(threewordToFull.get("MAR"))
print(threewordToFull.get("AUG","Invalid key"))