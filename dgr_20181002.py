Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print (123)
123
>>> print ("hello")
hello
>>> class = 3
SyntaxError: invalid syntax
>>> None = 3
SyntaxError: cannot assign to None
>>> x = 12
>>> y = 22
>>> variable"x"
SyntaxError: invalid syntax
>>> var(x)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    var(x)
NameError: name 'var' is not defined
>>> vars(x)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    vars(x)
TypeError: vars() argument must have __dict__ attribute
>>> vars("x")

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    vars("x")
TypeError: vars() argument must have __dict__ attribute
>>> x
12
>>> y
22
>>> x = 100
>>> x
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 22, '__name__': '__main__', '__doc__': None}
>>> _speed = 10
>>> _sp

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    _sp
NameError: name '_sp' is not defined
>>> _speed
10
>>> ("mnemonic" = "memory aid")
SyntaxError: invalid syntax
>>> ("mnemonic")
'mnemonic'
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '_speed': 10, '__package__': None, 'x': 100, 'y': 22, '__name__': '__main__', '__doc__': None}
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd
>>> x1q3z9ocd = 35.0
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '_speed': 10, '__package__': None, 'x1q3z9afd': 12.5, 'x1q3p9afd': 437.5, 'x': 100, 'y': 22, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x = 3.9 * x * (1-x)
>>> x
-38610.0
>>> x = 3.9 * x * ( 1-x )
>>> x
-5814005769.0
>>> x = 3.9*x*(1-x)
>>> x
-1.3183038604233921e+20
>>> x = 3.9*x*(1 - x)
>>> x
-6.777907766788153e+40
>>> x = 12.2
>>> x = 3.9*x*(1 - x)
>>> x
-532.896
>>> xx = 2
>>> xx
2
>>> xx = xx + 2
>>> print(xx)
4
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> x
7
>>> a = 1 + 4
>>> print(a)
5
>>> b = "hello" + "world"
>>> print(b)
helloworld
>>> b = "hello " + "world"
>>> print(b)
hello world
>>> b = b + 1

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b = b + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(b)
<type 'str'>
>>> type("hello")
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type(xx)
<type 'int'>
>>> xx = 11.1
>>> type(xx)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(11.1)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> print(float(0.23) + 10)
10.23
>>> i = 24
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
24.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> age = "18"
>>> type(age)
<type 'str'>
>>> print(age + 1)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(age + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> _age = int(age)
>>> type(_age)
<type 'int'>
>>> print(_age + 1)
19
>>> frs = "hello Andrew"
>>> frsn = int(frs)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    frsn = int(frs)
ValueError: invalid literal for int() with base 10: 'hello Andrew'
>>> nam = input("Who are you& ")
Who are you& 

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    nam = input("Who are you& ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input("Who are you? ")
Who are you? Andrew

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    nam = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> nam

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    nam
NameError: name 'nam' is not defined
>>> script1.py

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    script1.py
NameError: name 'script1' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    nam = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? q

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    s = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'q' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    question = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    question = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? q

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    question = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'q' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    mname = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> nam = input("Who are you? ")
Who are you? Andrew

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    nam = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> nam = input("Who are you? ")user
SyntaxError: invalid syntax
>>> nam = input("Who are you? ")
Who are you? user

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    nam = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'user' is not defined
>>> nam = input("Who are you? ")
Who are you? x

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    nam = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? 1
('Welcome', 1)
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    mname = input("Who are you? ")
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    mname = input('Who are you? ')
  File "<string>", line 1, in <module>
NameError: name 'Andrew' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? 1
('Welcome', 1)
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? asdas

Traceback (most recent call last):
  File "/home/user/RTR105/script1.py", line 1, in <module>
    mname = input('Who are you? ')
  File "<string>", line 1, in <module>
NameError: name 'asdas' is not defined
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
Who are you? Andrew
('Welcome', 'Andrew')
>>> efl = input("Europe floor?")
Europe floor? 1
>>> ufl = int(efl) + 1
>>> print("US floor", ufl)
('US floor', 2)
>>> #thats my name
>>> name = raw_input("Enter ur name:")
Enter ur name:Andrew
>>> 5/4
1
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
What time is it? 10
What rate is it? 2.3
('U should pay: ', 23.0)
>>> 
=================== RESTART: /home/user/RTR105/script1.py ===================
How much u where here? 23
What rate is it? 1.762
('U should pay: ', 40.526)
>>> 
