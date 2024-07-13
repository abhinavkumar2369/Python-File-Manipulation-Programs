
file = open("01_example.txt",'r')

for line in file:
    print(line.strip())

file.close()