# files2.py - adding names to the student grade list

# as before...
grades_file = open("grades.csv", "r")
header = grades_file.readline()
data = grades_file.readlines()
grades_file.close()

# now also read in id_to_names.csv
name_file = open("id_to_names.csv", "r")
# no header in this file
name_data = name_file.readlines()
name_file.close()

# turn id_to_names data into a dictionary

# make an empty dictionary
names_dict = {}
# HINT - whenever you make a dictionary - explain in comments
# what the keys and values are going to be, and what their types are!
# Here keys will be id number, values will be student name, both as strings

for line in name_data:   # go through all students
    # split line into two on the comma
    items = line.split(",")
    id_number = items[0]     # id is the first item - can stay as a string
    name = items[1].strip()  # will have a newline at the end - will matter
#                              this time as we are printing it - so have
#                              to strip it off

    # add id:name to our dictionary
    names_dict[id_number] = name

for line in data:       # for every line in the original file...
    # as before
    split_line = line.split(",")
    student_id = split_line[0]   # is a string - fine for using as key later...
    y1 = int(split_line[1])
    y2 = int(split_line[2])
    y3 = int(split_line[3])
    y4 = int(split_line[4])
    overall_student_grade = .075 * y1 + .2 * y2 + .3625 * y3 + .3625 * y4

    # get name by looking up id in the dictionary
    # testing to check it's actually there!
    if student_id in names_dict:
        name = names_dict[student_id]   # get name from dict...
    else:
        name = "NAME NOT FOUND"         # or set to NAME NOT FOUND

    # output the result for this student
    print(f"Student {student_id} ({name}): "
          f"Overall grade is {overall_student_grade:.1f}")
