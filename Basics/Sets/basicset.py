list1 = [1,2,2,3]

print(list1)

set1 = {1,2,2,3}
print(set1) # set will print only the unique values

set2 ={}
print(type(set2)) # it will print dict, sinc both dict and set syntax is {}

set3 = set({})
print(type(set3)) # to create empty set we have to explictly define as set like this

set3.add(5)
set3.add(6)
set3.add(5)

print(set3)

# set3.remove(7) # if the entry is not in set, it will throw keyerror

# If you wan't ignore the error if that key not present in that set, go for discard

set3.discard(7)

# set3.clear() # it empty the set

print(set3.pop()) # pop will remove random element from the set

print(set3)

for key in set1:
    print(key)

if 3 in set1:
    print("3 is present in set1")    
else:
    print("3 is not present")   

odd = {1,3,5,7,9}
even = {2,4,6,8}
prime = {2,5,7}  

print(odd.union(even))
print(even.intersection(prime))

set_1 = {1,2,3,4,5,6}

# set_2 = set_1

set_2 = set(set_1)
# set_2 = set_1.copy()

set_2.add(9)
print(set_1)
print(set_2)