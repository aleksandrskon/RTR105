Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /home/user/RTR105/test_3_20181009.py ===============
Hello
Fun
Zip
Hello
Fun
>>> big = max("Hello world")
>>> print(big)
w
>>> tiny = min("Hello world")
>>> print(tiny)
 
>>> print(float(99) / 100)
0.99
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(1 + 2 * float(3) / 4 - 5)
-2.5
>>> w

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> swal = "123"
>>> type(sval)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(sval)
NameError: name 'sval' is not defined
>>> type(swal)
<type 'str'>
>>> print(swal + 1)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(swal + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(swal)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = "hello bob"
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> def print_lyrics()
SyntaxError: invalid syntax
>>> 
=============== RESTART: /home/user/RTR105/test_3_20181009.py ===============
>>> print_lyrics()
I:am a lumberjack, and i:m okay.
I sleep all night and i work all day.
>>> def greet(lang):
	if lang == "es"
	
SyntaxError: invalid syntax
>>> def greet(lang):
	if lang == "es":
		print("Hola")
	elif lang == "fr":
		print("Bonjour")
	else:
		print("Hello")

		
>>> greet("en")
Hello
>>> greet("es")
Hola
>>> greet("fr")
Bonjour
>>> print(greet("en"),"Glenn")
Hello
(None, 'Glenn')
>>> def greet()
SyntaxError: invalid syntax
>>> def greet():
	return "Hello"
print(greet(), "Glenn")
SyntaxError: invalid syntax
>>> def greet():
	return "Hello"

>>> print(greet(), "Glenn")
('Hello', 'Glenn')
>>> print(greet("en"),"Glenn")

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(greet("en"),"Glenn")
TypeError: greet() takes no arguments (1 given)
>>> print(greet("en"), "Glenn")

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(greet("en"), "Glenn")
TypeError: greet() takes no arguments (1 given)
>>> print(greet("en"),"Glenn")

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(greet("en"),"Glenn")
TypeError: greet() takes no arguments (1 given)
>>> print(greet("en"),"Glenn")

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(greet("en"),"Glenn")
TypeError: greet() takes no arguments (1 given)
>>> def addtwo(a.b):
	
SyntaxError: invalid syntax
>>> def addtwo(a,b):
	added = a + b
	return added

>>> x = addtwo(3,5)
>>> print(x)
8
>>> 
