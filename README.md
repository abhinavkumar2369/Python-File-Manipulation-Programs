## Programs 📝

### 1. Reading the content of file.

```py
# Open the file
file = open("01_example.txt", "r")


# Read the content of the file
# Returns the content of the file as a string

print(file.read())
file.seek(0)


# Read the content of the file line by line using readlines() method
# Returns a list of lines in the file

print(file.readlines())
file.seek(0)

```

### 2. Reading line by line.

```py
# Opening the file
file = open("01_example.txt",'r')

# Iterating through the file line by line
for line in file:
    print(line.strip())

# Closing the file
file.close()
```


### 3. Count the number of lines in file.

```py
# Opening File
file = open("01_example.txt",'r')

# Counting number of lines as file.readlines returns all line in form of list.
count = len(file.readlines())

print("The no. of lines is --->",count)

# Closing the files
file.close()
```


### 4. Copy Content from One File to Another.

```py
#  Date Copying
#  [01_example.txt]   ------->   [output.txt]


# Current File
file = open("01_example.txt",'r')

# Another File
output = open("output.txt",'w')

# Copying Data
output.write(file.read())


# File closing
file.close()
output.close()
```

### Write a Python program to append to an existing file.

```py
# Opening the file in append mode
file = open("01_example.txt","a+")

# Writing to the end of the file as file pointer will be at end.
file.write("This is the appended line.")


# Closing the file
file.close()
```
