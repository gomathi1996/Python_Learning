# List -> Multiple values of different datatype can be stored in a variable
# It can also have duplicate values

name = ["gomathi","monika","praveen",2,4.5,True]

print(name)

print(name[2])

print(name[-2]) # print value from last index
print(name[1:])
print(name[1:2])
print(name[2:4]) # First index value - included, Second index value - excluded
print(name[:3])

list_var=[60,"Gomathi",78,[90]]
print(type(list_var[3]))

# Built-in Functions in list
names = ["Kholi","Dhoni","Sachin","Kholi"]
age = [32,40,52]

print(names.count("Kholi")) # print no. of times specific value is present in list

names.sort() # Sort list in ascending value
print(names)

names.reverse() # Sort list in reverse order
print(names)

name1 = names.copy() # copy list to another variable
print(name1)

names.extend(age) # Concatenate two lists
print(names)

names.append("Rahul") # Add new value to existing listing at last index
print(names)

names.insert(2,"Dawan") # Add new value to existing listing at specific index
print(names)

names.remove("Dhoni") # Remove specific value from the list
print(names)

names.pop() # Remove the last index value from the list
print(names)

print(names.index("Sachin"))

names.clear() # Remove all the value from the list
print(names)
