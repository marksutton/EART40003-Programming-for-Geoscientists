# demo_2_grades.py - work out grade for this module & optionally classification

# get the coursework marks from the user
coursework1 = float(input("Mark for CW 1 (out of 10): "))
coursework2 = float(input("Mark for CW 2 (out of 15): "))
coursework3 = float(input("Mark for CW 3 (out of 10): "))
coursework4 = float(input("Mark for CW 4 (out of 35): "))

# get a string y or n to see if they want a classification of their grade
yesOrNo = input("Do you also want a classification? (y/n): ")

# divide all courseworks by what they were out of
coursework1 = coursework1 / 10
coursework2 = coursework2 / 15
coursework3 = coursework3 / 10
coursework4 = coursework4 / 35

# work out weighted mark
grade = 0.2*coursework1 + 0.2*coursework2 + 0.2*coursework3 + 0.4*coursework4

# grade variable is going to be 0-1 - multiply by 100 to get a percentage
grade = grade * 100

# print grade (with blank lines before for clarity in output)
print(f"\n\nYour overall mark is {grade:.0f}")

if yesOrNo == "y":
    if grade >= 70:
        print("... which is a 1st")
    elif grade >= 60:
        print("... which is a 2i")
    elif grade >= 50:
        print("... which is a 2ii")
    elif grade >= 40:
        print("... which is a 3rd")
    else:
        print("... which is a fail")

print("Reached end of program")   # added to show where flow goes after 'if'