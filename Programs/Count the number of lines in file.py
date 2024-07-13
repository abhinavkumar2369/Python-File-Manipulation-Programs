
file = open("01_example.txt",'r')

count = len(file.readlines())

print("The no. of lines is --->",count)

file.close()