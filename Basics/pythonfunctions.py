# Functions - group of lines of code/statement
# Write once and reuse wherever required

def print_name(name,age):
    # name = "John" # local variable
    print(f'My name is {name} and my age is {age}')

print_name("Dhoni",39)    # parameters

def square(num):    
    return num * num  
   
print(square(4))     # calling the function with no argument