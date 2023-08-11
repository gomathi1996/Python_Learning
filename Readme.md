# Variable : 
## to store single value 
### Syntax
```python
var1="value1" 
```

# List: 
## to store multiple value and it's mutable 

### Syntax

```python
name=["gomathi","Monika",123]
```

# Tuple: 
## to store multiple value and it's immutable 

### Syntax

```python
name=("gomathi","Monika",123)
```

# Functions:

Functions - group of lines of code/statement
Write once and reuse wherever required

function name should be seperated by underscode for better readability

function name starts with def keyword

## Return statement

a special statement that you can use inside a function or method to send the function's result back to the caller.

A return statement ends the execution of a function, and returns control to the calling function.

# If statement

The IF statement is a decision-making statement that guides a program to make decisions based on specified criteria. The IF statement executes one set of code if a specified condition is met (TRUE) or another set of code evaluates to FALSE.

### and - both statement should be true, 
### or - either one of the statemnet should be true, 
### not - opposite of that statement
### if,elif,else  

# Dictionaries

Store Key, value pair
key should be unique and it can be any type

## Syntax

```python
threewordToFull = {
    0: "January",
    "FEB": "Febuary",
    "MAR": "March"
}
```
# Loops

contains instructions that continually repeat until a certain condition is reached

## While loop

```python
while i<=10:
    print(f"The value of the variable is {i}") #print statement
    i = i+1
```
## For loop

```python
for x in range (6):
    print(x)
    x = x+1

for j in "gomathi":
    print(j)  

cricketer = ["kohli","Dhoni","Sachin"]
for cricketers_name in cricketer :
    print ("Cricketer name is ",cricketers_name )        
```
## Nested loop
2D list/ Matrix List

To store multiple list in single variable

```python
for row in num:
    for col in row:
        print(col)
```

# Comments
enhance the readability of the code and help the programmers to understand the code very carefully.

## Single line comment

```python
# Single line comment
```

## Multiple line comment


```
Multiple line comment
second line
Third Line
``` 
# Try Except Statement
enables applications to gain control of a program when events that normally terminate execution occur

used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.

```python
try:
    num = int(input("Enter number : "))
    print(num)
except:
    print("Invalid Input")
```
# Files

1. Open and close the files

r - read mode
w - write mode (Flush all the existing value and keep only the new value)
a - append mode (Add the new value along with existing values)
r+ - read and write

# Modules

Write common functions in a module and import it wherever required

```python
# Method 1
import commonmodule
commonmodule.print_captain()
commonmodule.print_vice_captain()

# Method 2
from commonmodule import print_captain
print_captain()

# Method 3
from commonmodule import print_captain as pc
pc()
```

# Classess and Objects

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state.

class should below function

```python
class Batsman:

# this is the default function and should be created in all the class and it should have self as parameters

    def __init__(self,name,age,ipl_team):
        self.name = name
        self.age = age
        self.ipl_team = ipl_team
```

### Object Creation

```python
Batsman1 = Batsman("virat",32,"RCB")
Batsman2 = Batsman("Dhoni",45,"CSK")
```

# Inheritance
allows us to define a class that inherits all the methods and properties from another class. 
Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

```python
class Human:

    def name(self):
        print('Name')

    def age(self):
        print('Age')    
      

class Batsman(Human):
    def runs(self):
        print("Runs scored")
    
    
batsmn1 = Batsman()
batsmn1.age()
```
# Sets

Similar as List but it won't allow duplicate entries
It prints only the unique entries
It store in random order

### Union and Intersection in sets

set1.union(set2)
set1.intersection(set2)

### copy one set to another

set2 = set1.copy()  or set2 = set(set1) -> when we add value to set2, it won't add it in set1

set2 = set1 -> when we add value to set2, it will get added in set1 also.
