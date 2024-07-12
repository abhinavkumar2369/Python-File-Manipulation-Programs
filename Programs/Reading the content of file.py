import os

# Open the file
file = open("example.txt", "r")



# Read the content of the file
# Returns the content of the file as a string

print(file.read())
file.seek(0)




# Read the content of the file line by line using readlines() method
# Returns a list of lines in the file

print(file.readlines())
file.seek(0)




# Read the content of the file line by line using a for loop
for line in file.readlines():
    print(line.strip())
file.seek(0)




# Close the file
file.close()