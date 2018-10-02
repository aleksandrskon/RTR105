Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> >>> 
print(123)
SyntaxError: invalid syntax
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello world")
Hello world
>>> false

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> x = 12.2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, '__name__': '__main__', '__doc__': None}
>>> y = 14
>>> x = 100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> z = _speed

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    z = _speed
NameError: name '_speed' is not defined
>>> z =_speed

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    z =_speed
NameError: name '_speed' is not defined
>>> x = _speed

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = _speed
NameError: name '_speed' is not defined
>>> x1q3z9ocd = 35.0
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
437.5
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9 * x * ( 1 - x )
>>> x=0.6
>>> print(x)
0.6
>>> x = 3.9 * x * ( 1 - x )
>>> print(x)
0.936
>>> xx = 2
>>> xx = xx +2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = "hello" + "there"
>>> print(eee)
hellothere
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type("hello")
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> sval = "123"
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv = "hello bob"
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input(Who are you?")
	    
SyntaxError: invalid syntax
>>> nam = input("Who are you?")
Who are you?5
>>> print("Welcome", nam)
('Welcome', 5)
>>> inp = input("Europe floor?")
Europe floor?1
>>> usf = int(inp) + 1
>>> print("US floor", usf)
('US floor', 2)
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
437.5
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
Enter Hours35
Enter Rate2.75
96.25
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
Enter Hours35
Enter Rate2.75
96.25
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
Enter Hours35
Enter Rate2.75
96.25
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
Enter Hours 35 2.75

Traceback (most recent call last):
  File "/home/user/RTR105/test_2.py", line 1, in <module>
    a = input("Enter Hours ")
  File "<string>", line 1
    35 2.75
          ^
SyntaxError: unexpected EOF while parsing
>>> 
==================== RESTART: /home/user/RTR105/test_2.py ====================
Enter Hours 35
Enter Rate 2.75
96.25
>>> 
