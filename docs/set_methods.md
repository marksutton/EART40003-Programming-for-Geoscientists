set (built-in set class)
=======================

These are methods not functions, so the syntax uses the ‘.’ after an object of type list. For example, use `myset.clear()` not `clear(myset)` to clear the set.

Some set methods return a new modified copy of the set, others modify it in place. Read the descriptions!

**clear() return type: N/A**
<br />Clears the set, i.e. deletes all items within it.

**copy() return type: set**	<br />Returns a copy of the set. This is NOT the same as using =. 
You CAN do `set_a = set_b`, but that doesn't make a copy – `set_a` just refers to the same copy of the set as `set_b`, so if you change `set_a`, you are also changing `set_b`. 
Use copy to make a real copy you can modify separately.

**remove(element) return type: N/A**	<br />Removes the element specified from the set, or throws an exception if no such element exists.

**difference(otherset) return type: set**	<br />Calculates the difference between sets, i.e. removes if any element of the set is also in `otherset`, it is removed. 
This is the same as using the – operator (so `a.difference(b)` is the same as `a-b`, if a and b are both sets).

**union(othersets) return type: set**<br />	Returns the union of the set and all sets in `othersets`
(`othersets` can be more than one set, as a list of arguments separated by commas). The intersection is a set containing all elements that are in ANY of the sets. 

**pop() return type: varies**	<br />Removes a random item from the set, and returns it. Would be useful for implementing dealing in a card game for instance!
