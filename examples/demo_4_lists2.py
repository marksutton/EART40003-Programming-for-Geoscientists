# lists2.py - more lists, range function in for loops

square_numbers = []    # make an empty list

for i in range(1, 11):           # gives numbers 1-10
    # square_numbers[i] = i*i      # WON'T work - index has to exist
    square_numbers.append(i*i)   # this works - append each number to list


print("\nSquare numbers:")
print(square_numbers)

for i in range(1, 11, 3):           # gives numbers 1, 4, 7, 10
    square_numbers[i-1] -= 1        # subtract 1 from every third number
    # Why do we need the -1 in the index?

print("\nModified square numbers:")
print(square_numbers)            # print out modified list

print(f"\nSum of list: {sum(square_numbers)}")       # sum function
print(f"Count of items in list: {len(square_numbers)}")       # len function


