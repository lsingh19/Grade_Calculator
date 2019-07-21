
# Project Name: Grades
# Creator: lsingh19
# Purpose: To calculate the GPA and WAM of the courses done by a student
# Last Modified: 21/07/2019

# the statement will open a file at the directory given
# note:  '\\' must be used when specifying the directory of the file
# 'w' means to write in the file. This will overwrite the file
# 'a' means append onto the file (add to the file)
# 'r' means to read the file - error if the file does not exist
# 'r+' means to read and write on the file
#  'w+' means to read and write on the file, if file doesn't exist then it will create a new file.
#       if it exist then it will overwrite it.

results = []
# There is no need to close the file when using a 'with' statement
f = open("C:\\Projects\\grades.txt", "r")
next(f)
next(f)
for line in f:
    line = line.replace("\t", '')
    line = line.replace('\n', '')
    tokens = line.split(" ")
    print(tokens)
    if tokens[0] == 'Results' or line == '':
        break
    else:
        results.append(tokens)

f.close()
print(results)

f = open("C:\\Projects\\grades.txt", "w")
f.write("Course Unit Weight Mark Grade\n")
f.write("---------------------------------------------------\n")
for i in results:
    for p in i:
        f.write(p + " ")
    f.write("\n")


def grade(x):
    if x == 'HD':
        return 7
    elif x == 'D':
        return 6
    elif x == 'C':
        return 5
    elif x == 'P':
        return 4
    elif x == 'UP':
        return 4
    elif x == 'FF':
        return 0
    else:
        return -1


def wam(weight):
    if weight == 1 or weight == 1000:
        return 1
    elif weight == 2 or weight == 2000:
        return 2
    elif weight == 3 or weight == 3000:
        return 3
    elif weight == 4 or weight == 4000:
        return 4
    elif weight == 5 or weight == 5000:
        return 5
    elif weight == 6 or weight == 6000:
        return 6
    else:
        return -1


def class_awarded(mark):
    if mark >= 85:
        return 'Honours Class 1'
    elif mark >= 75 or mark <= 84:
        return 'Honours Class 2 Division 1'
    elif mark >= 65 or mark <= 74:
        return 'Honours Class 2 Division 2'
    elif mark >= 50 or mark <= 64:
        return 'Honours Class 3'
    else:
        return "Fail"


num = 0
unit_value = 0
for i in results:
    z = grade(i[4])
    if z == -1:
        print("Error: the grade provided for " + i[0] + " is an invalid grade")
    else:
        num = num + int(i[1]) * int(z)
        unit_value = unit_value + int(i[1])

gpa = num/unit_value
print(gpa)

top = 0
bottom = 0
for i in results:
    top = top + (int(i[3]) * int(i[1]) * wam(int(i[2])))
    bottom = bottom + (int(i[1]) * wam(int(i[2])))

weighted_average_mark = top/bottom

f.write("\n\nResults\n")
f.write("---------------------------------------------------")
f.write("\nGrade Point Average (GPA): " + str(gpa))
f.write("\n---------------------------------------------------\n")
f.write("Weighted Average Mark (WAM): " +str(weighted_average_mark))
f.write("\nClass Awarded: " + class_awarded(weighted_average_mark))

# must close the file before the program closes or errors will occur.
f.close()