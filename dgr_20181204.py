Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> org = "To be or not to be"
>>> key = 50
>>> original[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    original[0]
NameError: name 'original' is not defined
>>> org[0]
'T'
>>> ord(org[0])
84
>>> bin(ord(org[0]))
'0b1010100'
>>> chr(84)
'T'
>>> ord(org[0]) ^ key
102
>>> org[0]
'T'
>>> chr(ord(org[0]) ^ key)
'f'
>>> message = []
>>> for i in range(len(original)):
	message.append(chr(ord(org[i]) ^ key))

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for i in range(len(original)):
NameError: name 'original' is not defined
>>> for i in range(len(original)):
	message.append(chr(ord(org[i]) ^ key))

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for i in range(len(original)):
NameError: name 'original' is not defined
>>> for i in range(len(org)):
	message.append(chr(ord(org[i]) ^ key))

>>> for i in range(len(org)):
	message = message + (chr(ord(org[i]) ^ key))

Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    message = message + (chr(ord(org[i]) ^ key))
TypeError: can only concatenate list (not "str") to list
>>> for i in range(len(org)):
	message = message + chr(ord(org[i]) ^ key)

Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    message = message + chr(ord(org[i]) ^ key)
TypeError: can only concatenate list (not "str") to list
>>> message = []
>>> for i in range(len(org)):
	message = message + chr(ord(org[i]) ^ key)

Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    message = message + chr(ord(org[i]) ^ key)
TypeError: can only concatenate list (not "str") to list
>>> for i in range(len(org)):
	message = message + (chr(ord(org[i]) ^ key))

Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    message = message + (chr(ord(org[i]) ^ key))
TypeError: can only concatenate list (not "str") to list
>>> org = "To be or not to be"
>>> key = 50
>>> org[0]
'T'
>>> message = []
>>> for i in range(len(org)):
	message = message + chr(ord(org[i]) ^ key)

Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    message = message + chr(ord(org[i]) ^ key)
TypeError: can only concatenate list (not "str") to list
>>> for i in range(len(org)):
	message = message + chr(ord(org[i]) ^ key)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    message = message + chr(ord(org[i]) ^ key)
TypeError: can only concatenate list (not "str") to list
>>> original = "To be or not to be"
>>> key = 50
>>> original[0]
'T'
>>> message = []
>>> for i in range(len(original)):
	message = message + chr(ord(original[i]) ^ key)

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    message = message + chr(ord(original[i]) ^ key)
TypeError: can only concatenate list (not "str") to list
>>> message = ""
>>> for i in range(len(original)):
	message = message + chr(ord(original[i]) ^ key)

	
>>> message
'f]\x12PW\x12]@\x12\\]F\x12F]\x12PW'
>>> result = ""
>>> for i in range(len(message)):
	result = result + chr(ord(message[i]) ^ key)

	
>>> 
>>> result
'To be or not to be'
>>> 
