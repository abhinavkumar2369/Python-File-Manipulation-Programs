#   Date Copying
 
#   [01_example.txt]   ------->   [output.txt]


# Current File
file = open("01_example.txt",'r')

# Another File
output = open("output.txt",'w')

# Copying Data
output.write(file.read())


# File closing
file.close()
output.close()