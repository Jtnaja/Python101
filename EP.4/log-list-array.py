Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
MaBox = []
box.append('JT','1')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    box.append('JT','1')
NameError: name 'box' is not defined
box.append('JT')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    box.append('JT')
NameError: name 'box' is not defined
MaBox.append('JT','1')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    MaBox.append('JT','1')
TypeError: list.append() takes exactly one argument (2 given)
MaBox.append('JT')
MaBox.append('kuy')
print(MaBox)
['JT', 'kuy']
print(Mabox[1])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(Mabox[1])
NameError: name 'Mabox' is not defined. Did you mean: 'MaBox'?
print(MaBox[1])
kuy
kuy
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    kuy
NameError: name 'kuy' is not defined
brand = {'pen':['pentel'],['fiberpaster']}
SyntaxError: incomplete input
brand = {'pen':['pentel'],['fiberpaster'],'pensill':['houseres','steadael'],'runber':'red'}
SyntaxError: ':' expected after dictionary key
>>> brand = {'pen':['pentel','fiberpaster'],'pensill':['houseres','steadael'],'runber':'red','blue'}
SyntaxError: incomplete input
>>> brand = {'pen':['pentel','fiberpaster'],'pensill':['houseres','steadael'],'runber':'red'}
>>> 
...  
>>> print(brand)
{'pen': ['pentel', 'fiberpaster'], 'pensill': ['houseres', 'steadael'], 'runber': 'red'}
>>> print(brand['pen'][-1])
fiberpaster
>>> print(brand['pensill'][-1])
steadael
