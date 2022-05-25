# py_tools
py_tools is a powerful python library that does some basic work for you.
### How to Use:
Download the zip file and extract it. Then copy py_tools.py and paste it in the directory in which you have your python file.
___
## Functions:
### 1) Arithmetic_Operation_With_Lists(listToBeCalculated, Operation)
This helps you to calculate the sum of the numbers in a list.
For example:
#### Code:
```python
import py_tools as py

num_list = [1, 2, 3, 4]
py.Arithmetic_Operation_With_Lists(num_list, "+")
py.Arithmetic_Operation_With_Lists(num_list, "-")
py.Arithmetic_Operation_With_Lists(num_list, "*")
py.Arithmetic_Operation_With_Lists(num_list, "/")
```
#### Result:
```
10
-8
24
0.0416666667
```
#### !!!!The ORDER OF NUMBERS in a list is very important.
### 2) Join_Everything_In_List(listToBeJoined)
This combines everything in the list, even if it is a number.
For example:
#### Code:
```python
import py_tools as py

value_list = ["Hello", " ", "World", "!"]
py.Join_Everything_In_List(value_list)
```
#### Result:
```
Hello World!
```
### 3) Get_Index_Of_A_Character_In_List(listSpecified, Item)
It gets the item number of an item in the list.
For example:
#### Code:
```python
import py_tools as py

value_list = ["Hello", " ", "World", "!"]
py.Get_Index_Of_A_Character_In_List(value_list, "World")
```
#### Result:
```
2
```
