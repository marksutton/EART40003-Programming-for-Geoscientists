
# files.py - example of opening, and processing a file

grades_file = open("grades.csv", "r")

header = grades_file.readline()     # First line is a header - read to skip
data = grades_file.readlines()      # read rest of lines into data list

grades_file.close()

for line in data:       # for every line in the original file...
    # line is the full text of the line, commas and all
    split_line = line.split(",")    # split on commas into a list
    # split_line is now a list of the 5 values for this student

    # extract the ID number
    student_id = split_line[0]   # can stay as string - only going to print it

    # read in the year marks, converting to ints
    y1 = int(split_line[1])
    y2 = int(split_line[2])
    y3 = int(split_line[3])
    y4 = int(split_line[4])  # this has a newline at the end - but won't matter

    # work out a weighted mean - this IS the real formula
    overall_student_grade = .075 * y1 + .2 * y2 + .3625 * y3 + .3625 * y4

    # output the result for this student
    print(f"Student {student_id}: Grade is {overall_student_grade:.1f}")
