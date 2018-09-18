Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __b

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __b
NameError: name '__b' is not defined
>>> print  __builtins__.__doc__
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print __bui

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print __bui
NameError: name '__bui' is not defined
>>> print __builtins__.abs.__doc__
abs(number) -> number

Return the absolute value of the argument.
>>> abd(10)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    abd(10)
NameError: name 'abd' is not defined
>>> abs(10)
10
>>> __buil

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    __buil
NameError: name '__buil' is not defined
>>> __builtins__
<module '__builtin__' (built-in)>
>>> abs
<built-in function abs>
>>> abs(10-2_
    
SyntaxError: invalid syntax
>>> abs(10-2)
8
>>> a = 10
>>> a = ?
SyntaxError: invalid syntax
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> a * b

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a * b
NameError: name 'b' is not defined
>>> b = 2
>>> a* b
40
>>> a*b*b*a
1600
>>> a*a*A*A*A*A*A*
SyntaxError: invalid syntax
>>> a*a*a*
SyntaxError: invalid syntax
>>> a.__doc__
"int(x=0) -> int or long\nint(x, base=10) -> int or long\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is floating point, the conversion truncates towards zero.\nIf x is outside the integer range, the function returns a long instead.\n\nIf x is not a number or if base is given, then x must be a string or\nUnicode object representing an integer literal in the given base.  The\nliteral can be preceded by '+' or '-' and be surrounded by whitespace.\nThe base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to\ninterpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> print a.__doc__
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> type(a)
<type 'int'>
>>> b = 1.5
>>> vars()
{'a': 20, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> print b.__doc+__

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print b.__doc+__
AttributeError: 'float' object has no attribute '__doc'
>>> print b.__doc__
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
>>> type(b)
<type 'float'>
>>> c = D

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c = D
NameError: name 'D' is not defined
>>> c = "D"
>>> a - c

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a - c
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> print c.__doc__
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
>>> type(c)
<type 'str'>
>>> print a + c

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print a + c
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print a c
SyntaxError: invalid syntax
>>> print a
20
>>> print c
D
>>> print "a c"
a c
>>> print a "c"
SyntaxError: invalid syntax
>>> burts = "t"
>>> burts = "T"
>>> ord(burts)
84
>>> hex(ord(burts))
'0x54'
>>> bin(ord(burts))
'0b1010100'
>>> 
