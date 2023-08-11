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

```python
```
Multiple line comment
second line
Third Line
``` 
```


