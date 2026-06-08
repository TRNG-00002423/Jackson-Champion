
file = open("data.txt", "r")

#Read entire file
content = file.read()
print(content)
#print("*"*20)

#Read one line
line = file.readline()
print(line)

#Read all lines
lines = file.readlines()
print(lines)

#Close File
file.close()