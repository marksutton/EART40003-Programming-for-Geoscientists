---
---
{% raw %}
# demo_3_string_handling.py

Return to [Demonstration programs](index.md).

````python
# string_handling.py

test_string = "hello world"   # test string

position = 4        # position in string for test

print(test_string[position])      # print the current character
print(test_string[:position])     # print start to current
print(test_string[position:])     # print current to end
print(test_string[position:position+3])   # print 3 chars. from current
print(test_string[-1])        # print the last character

print()         # print a blank line to space the output a bit


# some string 'methods'
print(test_string.capitalize())   # capitalize sets initial letter to capital

# s2 is first five of s, all set to upper case
test_string2 = test_string[:5].upper()

# print it - remember strings can be added like this
print("First five characters of test_string, in capitals: " + test_string2)

o_characters = test_string.count("o")  # count 'o' characters in test_string
o_percent = 100 * (o_characters / len(test_string))

print(f"There are {o_characters} 'o's in '{test_string}' (={o_percent:.1f}%).")
````
{% endraw %}
