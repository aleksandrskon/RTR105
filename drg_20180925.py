Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienamais Lietotajs, ludzu ievadi vienu skaitli:")
Cienamais Lietotajs, ludzu ievadi vienu skaitli:10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienamais Lietotajs, ludzu ievadi vienu skaitli:")
Cienamais Lietotajs, ludzu ievadi vienu skaitli:10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_maingais

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mans_maingais
NameError: name 'mans_maingais' is not defined
>>> mans_mainigais
10
>>> mans_mainigais = input("Cienamais Lietotajs, ludzu ievadi vienu skaitli:")
Cienamais Lietotajs, ludzu ievadi vienu skaitli:20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigais)
<type 'int'>
>>> 
>>> f5

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    f5
NameError: name 'f5' is not defined
>>> 
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:7
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', 'mans_mainigais': 7, '__package__': None, 'x': 49, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:3
mans_mainigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:1
mans_mainigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 5, in <module>
    print("mans_mainigais = %d%"(mans_mainigais))
TypeError: 'str' object is not callable
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:12
mans_mainigais = 12
vai tu esi ievadijis skaitli: 12
vel atmina tagad ir ari mainigais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:5
mans_mainigais =      5.000
vai tu esi ievadijis skaitli:     5.0000
vel atmina tagad ir ari mainigais x =      25.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:8.5445
mans_mainigais =     8.54
vai tu esi ievadijis skaitli:      9
vel atmina tagad ir ari mainigais x =           73.0084802
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:5
mans_mainigais =      5.000
vai tu esi ievadijis skaitli:     5.0000
vel atmina tagad ir ari mainigais x =      25.0000000
>>> type(mans_mainigais)
<type 'int'>
>>> type(mans_mainigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi vienu skaitli:8
mans_mainigais =      8.000
vai tu esi ievadijis skaitli:     8.0000
vel atmina tagad ir ari mainigais x =      64.0000000
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi simbolu rindi:4

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi simbolu rindi:5
mans_mainigais = 5
vai tu esi ievadijis skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vel atmina tagad ir ari mainigais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienamais Lietotajs, ludzu, ievadi simbolu rindi:8
mans_mainigais = 8
vai tu esi ievadijis skaitli: 8

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vel atmina tagad ir ari mainigais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
