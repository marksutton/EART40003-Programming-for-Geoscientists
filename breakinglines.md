Breaking up long lines
=====================

Sometimes your lines will get too long - you should keep them under 80 characters. 
You can break lines with \ like so:

<pre>variable_with_a_possibly_over_verbose_name =\
      not_quite_so_verbose_variable_name * 2
</pre>

Or inside brackets, or square brackets, you can just put a line break in without worrying, e.g. 

<pre>a = (100 + b
          * c + 20)
</pre>

If you do this, stylistically the continuation should line up with the first character under the bracket on the line above.

Breaking lines that contain long strings is harder. If you have

<pre>print("this is a very very very very very very very very very very very very very long string")
</pre>

Your options are:

<pre>
print("this is a very very very very very very very "
      + "very very very very very very very very very "
      + "very very long string")
</pre>

Or the version below – if there are two strings next to each other without a plus, python just joins them anyway

<pre>
print("this is a very very very very very very very "
      "very very very very very very very very very "
      "very very long string")
</pre>

Note as well that 'f' strings need a new 'f' on each line, so
<pre>
print(f"{variable1} and "
      f"{variable2}")
</pre>

