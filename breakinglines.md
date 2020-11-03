Breaking up long lines
=====================

Sometimes your lines will get too long (flake8 will complain, and it IS best to avoid them). 
You can break lines with \ like so:

<pre>variable_with_a_possibly_over_verbose_name =\
      not_quite_so_verbose_variable_name * 2
</pre>

Or inside brackets, or square brackets, you can just put a line break in without worrying, e.g. 

<pre>print(“this is a number %g” 
      % (my_number))
</pre>

If you do this, flake8 likes the continuation to line up with the first character under the bracket on the line above.

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
