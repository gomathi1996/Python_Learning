myfamily = open("family.txt","r")

print(myfamily.readable()) # Able to read the file or not

# print(myfamily.read()) # read complete file

# print(myfamily.readline()) # read line by line from the file and here it reads only the first line
# print(myfamily.readline()) # reads the second line
# print(myfamily.readline()) # reads the third line

# print(myfamily.readlines()) # read all the lines and print in the form of list

print(myfamily.readlines()[2])

myfamily.close()
