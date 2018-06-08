user_file = input("enter file name: ")
with open ('lab6file.txt') as file:
	file_lines = file.readlines()
print(file_lines)
file.close()
for line in file_lines:
	print(line)