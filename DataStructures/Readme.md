# DataStructures
is a way of organizing data so that it can be accessed more efficiently depending upon the situation.

1. Store
2. Search
3. Modify - Add, delete

# Big O Notation - Measuring Efficiency
is a tool used to describe the time complexity of algorithms.
It calculates the time taken to run an algorithm as the input grows. 
In other words, it calculates the worst-case time complexity of an algorithm

O(1) O(logn) O(n) O(n logn) O(n^2) O(2^n)
Best-------------------------------> Worst

# Array
Stores group of values of same type
Stores values in memeory continously
Array size cannot be changed
Array index starts with 0
Array value is mutable

### Syntax
```bash
int a[5]
int b[] = {1,2,3,4,5}
```

## 2D Array / Matrix
```
int a[2][3] = {{1,2,3},{4,5,6}}
```

## Big O notation
```bash
Store - O(1)
Search - O(N)
Add - O(N)
Delete - O(N)
```

# Stack
Pile of books - Last In First Out (LIFO)

### Stack methods
1. Push
2. Pop
3. Peek
4. Contains

### Push
Inserting element into stack
It won't return anything
```bash
stack.push("a") #Size= 1
```

### POP
Remove last element from stack 
```bash
stack.pop() # returns the removed element
```
### Peek
return last element from stack 
```bash
stack.peek() # returns the last element
```

### Contains
search element from stack 
```bash
stack.contains("a") # returns true/false
```

## Big O notation
```bash
Store - O(N)
Search - O(N)
Add - O(1)
Delete - O(1)
```
## Use case
Undo/Redo
Recursion
Back Button

# Queue
Standing in a queue - First In First Out (FIFO)
### Stack methods
1. Enqueue
2. Dequeue
3. Peek
4. Contains