# Variable names

Variable names in Python can be any length and can consist of uppercase and lowercase letters (`A-Z`, `a-z`), digits (`0-9`), and the underscore character (`_`). Most important, note that **they cannot include spaces!** An additional restriction is that, although a variable name can contain digits, **the first character of a variable name cannot be a digit**. There are also some reserved Python keywords which cannot be used as variable names, including `False`, `True`, `None`, `if`, `else`, `for`, `while`, `def`, `class`, `return` and `import`.

Variable names are **case sensitive** - so `MyVariable` is NOT the same variable as `Myvariable`. This is a common source of errors, so look out for it.

Variable names should be meaningful - they should help someone reading your code understand what the variable is used for. Avoid single-letter variables (I've used some in examples here, but just to save space). Don't worry about how long it takes to type longer names - Thonny has an auto-fill feature that will bring them up for you if you start typing - but a good maximum length though would be ~20 characters. Where variable names incorporate multiple words (recall that you can't use spaces), avoid just running them together (so `accelerationduetogravity` is bad - it's hard to read). In these cases you can use either:

- `accelerationDueToGravity` (this is called Camel Case)
- `AccelerationDueToGravity` (this is called Pascal Case)
- `acceleration_due_to_gravity` (using underscores for spaces - this is called snake case)

It doesn't really matter which of these you use, although the last one (snake case) is the most commonly used in Python, and is what I will use in my examples. What DOES matter though is that you are consistent.

[Return to the site index](index.md)
