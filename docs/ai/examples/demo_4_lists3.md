---
---
{% raw %}
# demo_4_lists3.py

Return to [Demonstration programs](index.md).

````python
# lists3.py - using join and split to manipulate text
# also demonstrates min, max, len, sort, and more list wrangling
# Purpose: Splits a sentence into a list of words, counts the words...
# ... and counts the letters in each word

sentence = input("Enter a sentence: ")  # input. So far - easy

# split method of string returns a list split by a passed string (here " ")
word_list = sentence.split(" ")  # word_list is now, well, the words as a list

# len gives length of list - how many words?
print(f"Word count: {len(word_list)}")

# sort method of list returns nothing - sorts list 'in place'
word_list.sort()
# sort works on numbers, text - anything sortable
# word_list should now be in order


# make a string of the character to join on...
newline_string = "\n"   # newline in this case - could be anything

# make a single string by joining word_list with newline_string
# join is a method of string (NOT a method of list - WHY??)
output_string = newline_string.join(word_list)

# print out my output_string - words in order.
print(f"Word list in alphabetical order is:\n{output_string}\n")


# now going to do letter_counting. Pay attention to this bit!

# first  - we want a list of all the word_lengths in same order as word_list

word_lengths = []   # make an empty list

for word in word_list:              # for every word in word_list (in order)
    word_lengths.append(len(word))  # add it's length to new list

print("Word Lengths: ")
print(word_lengths)     # prints the list - bit ugly as we get [] but OKish

# now we will make another new list to hold our counts of word lengths
# how long should it be? Up to the maximum word length we found above

# use max and min functions to find shortest/longest length from our list
max_word_length = max(word_lengths)
min_word_length = min(word_lengths)

print("Word Min Lengths: ")
print(min_word_length)
print("Word Max Lengths: ")
print(max_word_length)

# make our third list - this is going to be counts of word lengths
# so if there are five three letter words, word_length_counts[3] will be 5

# first, we need to give it the right number of elements, and set them to 0
word_length_counts = []     # make the list

# loop i value from 0 up to max_word_length (the +1 because of how range works)
for i in range(0, max_word_length+1):
    word_length_counts.append(0)    # add a 0 to the list

# word_length_counts now consists of the right number of 0s, so if longest word
# was of length 5, it will hold [0,0,0,0,0,0]
# We will never use element 0 as 0 length words are impossible...
# ... but list indices always start at zero, so we have to have it there
# we'll just make sure we never print it!

# this does the actual counting
for length in word_lengths:      # for every length in our word_lengths list...
    # add one to the correct word_length_count entry
    word_length_counts[length] += 1

# one more for loop to print them
# note we start at min_word_length to skip 0s and 1, 2 etc if they didn't occur
for i in range(min_word_length, max_word_length+1):
    print(f"{i} letter words: {word_length_counts[i]}")
````
{% endraw %}
