list (built-in string class)


These are methods not functions, so the syntax uses the ‘.’ after an object of type list. For example, use mylist.sort() not sort(mylist)to sort the elements of a list into order.

Note that unlike string methods, many of these don't just return a new modified copy of the list – they modify the original list in-place (and typically don't return anything). See descriptions.

Method:	Description
append(value) return type: N/A	Appends value to the end of the list. Value can be any valid Python object. Note that if you want to add another list to the end of this list, don't use append, which will create a single extra element of type list! Use extend instead, or add the lists with the + operator.

append modifies the list in-place, so doesn't return anything. 
count(element) return type: int	Counts how many times the element element occurs in the list, returning an integer. So [1,2,2,3,4,3,2,4,1,4,1].count(1) returns 3.
extend(newlist) return type: N/A	Adds the elements of newlist to the end of this list. Extend modifies the list in-place, so doesn't return anything.
insert(index, element) return type: N/A	Inserts a new element into the list at position index. 
pop(index) return type: varies	Removes the element at position index from the list, and returns it. Note that this is different from remove, which needs the value of the element, not the index number (and doesn't return anything).
remove(element) return type: N/A	Removes element from the list – note that this takes an element, not an index number (use pop instead if you want to do that). If the element doesn't exist, an exception is thrown. 
reverse() return type: N/A	Reverses the order of the list. Affects the list in-place, so doesn't return anything.
sort() return type: N/A	Sorts the list in-place, into numerical or alphabetical order. Does not return anything. NOTE – there IS also a sorted function (not a method) that does much the same thing. 


