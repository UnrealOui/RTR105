Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
>>> vars()
{'mans_mainiigais': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais
10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais type
SyntaxError: invalid syntax
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> type
<type 'type'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 5
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainiigais * mans_mainiigais
NameError: name 'mans_mainiigais' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainiigais * mans_mainiigais
NameError: name 'mans_mainiigais' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_maiinigais': 8, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 3, in <module>
    x = mans_mainiigais * mans_mainiigais
NameError: name 'mans_mainiigais' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_maiinigais': 8, '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> print x
64
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
mans_maiinigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
mans_maiinigais = 10
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 5, in <module>
    print("mans_maiinigais = %d"(mans_maiinigais))
TypeError: 'str' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
mans_maiinigais = 10
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
mans_maiinigais = 10
vai Tu esi ievadījis skaitli: 10
vēl atmiņā tagad ir arī mainīgais x = 100
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_maiinigais = 12
Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_maiinigais = 12
Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
fck u
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli, kas kvadrāra ir 144: 12
mans_maiinigais = 12
Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
Correct
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli, kas kvadrāra ir 144: 10
mans_maiinigais = 10
Tu esi ievadījis skaitli: 10
vēl atmiņā tagad ir arī mainīgais x = 100
Incorrect
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8.6549
mans_maiinigais =      8.655
Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir arī mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 1
mans_maiinigais =      1.000
Tu esi ievadījis skaitli:     1.0000
vēl atmiņā tagad ir arī mainīgais x =       1.0000000
>>> type(x)
<type 'int'>
>>> type(mans_maiinigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8.0
mans_maiinigais =      8.000
Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir arī mainīgais x =      64.0000000
>>> type(mans_maiinigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simboly rindu: suka

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_maiinigais * mans_maiinigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simboly rindu: aaa
mans_maiinigais = aaa
Tu esi ievadījis skaitli: aaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 9, in <module>
    print("vēl atmiņā tagad ir arī mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simboly rindu: Nice
mans_maiinigais = Nice
Tu esi ievadījis skaitli: Nice
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simboly rindu: FailFish
mans_maiinigais = FailFish
Tu esi ievadījis rindu: FailFish
>>> type(mans_maiinigais)
<type 'str'>
>>> 

