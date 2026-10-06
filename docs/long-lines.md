# Breaking up long lines

Sometimes your lines will get too long (the linter will complain, and it IS best to avoid them). You can break lines with \ like so:

```python
variable_with_a_possibly_over_verbose_name =\
      not_quite_so_verbose_variable_name * 2
```

Or inside brackets, or square brackets, you can just put a line break in without worrying, e.g.

```python
result = (first_value * second_value
          + third_value / fourth_value)
```

If you do this, linters like the continuation to line up with the first character under the bracket on the line above. Breaking lines that contain long strings is harder. If you have:

```python
print("this is a very very very very very very very very very very very very very long string")
```

Your options are:

```python
print("this is a very very very very very very very "
      + "very very very very very very very very very "
      + "very very long string")
```

Or the version below – if there are two strings next to each other without a plus, python just joins them anyway

```python
print("this is a very very very very very very very "
      "very very very very very very very very very "
      "very very long string")
```

[Return to the site index](index.md)
