# errors.py - catching errors and checking input - and flags

ok_flag = False  # Sets a 'flag' - bool used to control program

# Linter prefers 'is' to '==' here... but I don't think it matters
# You have my permission to ignore this linter warning!
while ok_flag == False:     # loop as long as ok_flag is false
    try:
        # Try the input and the conversion. Will throw ValueError if it can't.
        input_value = float(input("Enter a whole number 1-10 "))

        # ... will get here if line above didn't throw an exception
        if not input_value.is_integer():
            # ... if it wasn't an integer -
            print("Not a whole number, try again\n")
        else:
            # ... it WAS an integer... in range?
            if input_value < 1 or input_value > 10:
                # Nope!
                print("Outside range 1-10, try again\n")
            else:
                # If we get here it's fine - set flag to True...
                # ... which will stop the loop
                ok_flag = True
    # Catch the conversion error which throws ValueError
    except ValueError:
        print("Not a number, try again\n")
    # Catch any other errors that appear...
    except Exception:
        # Best practice: When catching exceptions, mention specific exceptions
        # whenever possible instead of using a bare except: clause. A bare
        # except: clause will catch SystemExit and KeyboardInterrupt
        # exceptions, making it harder to interrupt a program with Control-C,
        # and can disguise other problems. If you want to catch all exceptions
        # that signal program errors, use except Exception: instead.
        print("Unknown error, try again\n")

# MUST have a valid value for input_value when it gets here!
print(f"\nCarrying on using number {input_value:.0f}")

