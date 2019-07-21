
# the statement will open a file at the directory given
# note:  '\\' must be used when specifying the directory of the file
# 'w' means to write in the file. This will overwrite the file
# 'a' means append onto the file (add to the file)
# 'r' means to read the file - error if the file does not exist
# 'r+' means to read and write on the file
#  'w+' means to read and write on the file, if file doesn't exist then it will create a new file.
#       if it exist then it will overwrite it.

f = open("C:\\Projects\\grades.txt", "r")
f_close = open("C:\\Projects\\grades_result.txt", "w")

# f.write("\nI Love python")    writes on the current file
# print(f.read())               reads the entire file as a whole

# reads each line one by one in the file
for line in f:
    tokens = line.split(' ')    # splits the sentence into words (by a space in between)
    # print(str(tokens))
    f_close.write(" wordcount: " + str(len(tokens)) + " " + line)
    print(len(tokens))  # prints the number of words in the file

#
with open("C:\\Projects\\grades.txt", "r") as f:
    print(f.read())

# f.closed() - tells you if the file is closed or still open.

# must close the file before the program closes or errors will occur.
f.close()
f_close.close()