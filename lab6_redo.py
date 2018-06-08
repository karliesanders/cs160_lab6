_author_ = 'Karlie Sanders'

#user_file = input("enter file name: ")
#with open ('lab6file.txt', 'r+') as file:
#	file_lines = file.readlines()
#file.close()
#for line in file_lines:
#	print(line)

def main():

   user_file = input("enter file name:(lab6file.txt) ")
   with open('lab6file.txt') as file:
      file_lines = file.readlines()
      file.close()
   for line in file_lines:
      words = line.split()
      counts = {}
      for word in words:
          if word in counts.keys():
             counts[word] = counts[word] + 1
          else:
             counts[word] = 1

   for key in sorted(counts.keys()):
      print("the word {0} occurs {1} times".format(key,counts[key]))

main()

'''
File_name = input(“enter file name: “)
With open (file_name as file:
	File_lines = file.readlines()
file.close()
For line in file_lines:
	print(line)
'''