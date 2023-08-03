# Tuples is same as list
# List is mutable whereas Tuples are unmutable

# List is mutable
name_list = ["gomathi","monika","praveen"]
print(name_list)

name_list[0]="manoharan"
print(name_list)

# Tuples are unmutable

name_list1 = ("gomathi","monika","praveen")
print(name_list1)

name_list1[0]="manoharan" # TypeError: 'tuple' object does not support item assignment
print(name_list1)