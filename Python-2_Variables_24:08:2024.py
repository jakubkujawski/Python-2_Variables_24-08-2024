Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
2 + 3
5
x = 2
x + 3
5
y = 3
x + y
5
x = 9
x + y
12
x
9
abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
x + 10
19
_ + y
22
# _ - underscore means: use output of the previous operations
# _ + y = 22 because previous operation was 19 so 19 + y = 22

name = 'youtube'
name
'youtube'
name + 'rocks'
'youtuberocks'
name + ' rocks'
'youtube rocks'
name[0]
'y'
name[6]
'e'
name[8]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'e'
# -1 gives e because it starts from end from -1 to -7; -7 = y

name[-7]
'y'
name[0:2]
'yo'
#name[0:2] it gives letters 0 and 1 - it not includes 2

name[1:4]
'out'
name[1:]
'outube'
>>> #[1:] if I not specify last number it will go from 1 till the end
>>> 
>>> name[:4]
'yout'
>>> #[:4] if I not specify first namber it will start from the first letter and end on the number 3 not including number 4
>>> 
>>> name[3:10]
'tube'
>>> #[3:10] it starts from leetter 4 because is 0,1,2,3 and it ends on the last one which is 8 because we don't have 10 letters
>>> 
>>> name[0:3] = my
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    name[0:3] = my
NameError: name 'my' is not defined. Did you mean: 'y'?
>>> name[0] = R
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    name[0] = R
NameError: name 'R' is not defined
>>> # it does not work because strings in Python is immutable it means that I cannpt change them
>>> 
>>> 'my' = name[3:6]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 'my' + name[3:6]
'mytub'
>>> 'my' + name[3:]
'mytube'
>>> 
>>> myname = 'Jakub'
>>> len(myname)
5
>>> countryname = 'UnitedKingdom'
>>> len(countryname)
13
>>> # funcion len counts the length of the characters in string
