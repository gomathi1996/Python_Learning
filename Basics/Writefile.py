#append mode
# myfamily = open("family.txt","a")

# write mode
# myfamily = open("family.txt","w")

myfamily = open("test.txt","w") # If file name not exists, it will create a new file and append this value

myfamily.write("newmember - unkown") # \n - will add this value in next line , otherwise it will append in same cursor line


myfamily.close()