Methods for dict (built-in dictionary class)
======================

These are methods not functions, so the syntax uses the ‘.’ after an object of type list. 
For example, use `mydict.values()` not `values(mydict)` to get a list of the values.

Like list methods, (and unlike string methods), many of these don't just return a new modified copy of the dict – 
they modify the original list in-place (and typically don't return anything). See descriptions.



**clear() return type: N/A**
<br />Clears the dictionary, i.e. deletes all items within it. 

**copy() return type: dict**
<br />Returns a copy of the dictionary. This is NOT the same as using =. You CAN do dict_a = dict_b, but that doesn't make a copy –
dict_a just refers to the same copy of the dictionary as dict_b, 
so if you change dict_a, you are also changing dict_b. Use `copy` to make a real copy you can modify separately.

**keys() return type: list**
<br />Returns a Python list of the keys.

**pop(key) return type: varies**
<br />Removes the value (element) with the given key, and returns it. 

**update (newdict) return type: N/A**
<br />Adds all the key/value pairs from `newdict` to the dictionary. This affects the dictionary 'in-place', and doesn't return anything. 

**values() return type: list**
<br />Returns a Python list of the values.
