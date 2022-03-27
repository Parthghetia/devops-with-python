## Range

```python
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(5, 10, 3))
[5, 8]
```

## if elif else

```python
>>> if i == 45:
...     print('i is 45')
... elif i == 35:
...     print('i is 35')
... elif i%3 == 0:
...     print('multiple of 3')  
... else:
...     print('i dont know')
... 
multiple of 3
>>> cat = 'spot'
>>> if 's' in cat:
...     print("Found an S in cat")
...     if cat == "Sheeba":
...         print ("sheeba")
...     else:
...         print ("some other cat")
... else:
...      print("a cat without an s")
... 
Found an S in cat
some other cat
>>>
```

For loops and breaking a for loop with continue

```python
>>> for i in range(10):
...      x=i*2
...      print (x)
... 
0
2
4
6
8
10
12
14
16
18
```
Continue
```python
>>> for i in range(6):
...      if i == 3:
...           continue 
...      print (i)
... 
0
1
2
4
5
```

## While loops
This repeat a block as long as a condition evaluates to true
```python
>>> while count < 3:
...     print(f"count is {count}")
...     count +=1
... 
count is 0
count is 1
count is 2
```

It is essential to define a way to stop your loop. Otherwise it would be stuck. You could use a break statement to prevent this like so
```python
>>> count = 0
>>> while True:
...       print(f"The count is {count}")
...       if count > 5:
...           break 
...       count += 1
... 
The count is 0
The count is 1
The count is 2
The count is 3
The count is 4
The count is 5
The count is 6
```
## Handling Exceptions
This is our try to catch an error in our code and not allow our program to crash but print a friendly output to show what's up really. Here is a perfect example
```python
"""
requirement: create a list of people whom you think of the greatest thinkers of all time
pop the one that you think is the least greatest of all time
make sure to create a try block to catch an exception if your list of thinkers end
"""

thinkers = ['Parth', 'Einstein', 'Maria']

while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print ("I think we are out of great thinkers unfortunately")
        print (e)
        break
```
## Objects and classes in Python

```python
>>> class fancyCar():
...     wheels = 4
... 
# Instantiate a fancy car
>>> my_car=fancyCar()
# Access the class attribute
>>> my_car.wheels
4   
>>> class fancyCar():
...     def driveFast(self):
...             print("Driving so fast")
... 
>>> my_car=fancyCar()
# Invoke the method
>>> my_car.driveFast()
Driving so fast
```
driveFast is a method and wheels is an attribute of our class

## Sequences
- These include: list, tuple, range, string, binary types
- Sequences represents ordered and finite collection of items

### Sequence operations

```python
>>> 2 in [1,2,3]
True
>>> 'a' not in 'cat'
False
>>> 10 in range(12)
True
>>> 10 not in range(2, 4)
True
```

You can always reference the contents of a sequence using its index number like below (notice -1 starts from behind):
```python
>>> my_sequence = 'Bill Cheatham'
>>> my_sequence[0]
'B'
>>> my_sequence[2]
'l'
>>> my_sequence[12]
'm'
>>> my_sequence = "Bill Cheatham"
>>> my_sequence[–1]
'm'
>>> my_sequence.index('a')
8
>>
```

#### Use of slicing in sequences
You can produce a new sequence from another sequence using slicing. A slice appears by invoking a sequence with brackets containing optional start, stop and step arguments

my_sequence[start:stop:step]

Let's do this
```python
>>> my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> my_sequence[2:5]
['c', 'd', 'e']
>>> my_sequence[:5]
['a', 'b', 'c', 'd', 'e']
>>> my_sequence[3:]
['d', 'e', 'f', 'g']
```

Sequences share many operations for getting information about them and their contents:
```python
>>> my_sequence = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
>>> len(my_sequence)
12
>>> min(my_sequence)
0
>>> max(my_sequence)
4
>>> my_sequence.count(1)
3
```
## Lists
```python
>>> list()
[]
>>> list (range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list('Henry Miller')
['H', 'e', 'n', 'r', 'y', ' ', 'M', 'i', 'l', 'l', 'e', 'r']
```
Always remember lists could house lists like below
```
>>> empty=[]
>>> another_list=['Hello', 9 , empty]  
>>> another_list
['Hello', 9, []]
```
The best way to add items to a list is to append them
```python
>>> devops = ['K8s', 'Git']
>>> devops.append('openshift')
>>> devops
['K8s', 'Git', 'openshift']
```
Contents of one list can be added to another using extend like so:
```python
>>> devops = ['K8s', 'Git']
>>> devops.append('openshift')
>>> devops
['K8s', 'Git', 'openshift']
>>> k8s = ['services', 'pods']
>>> k8s.extend(devops)
>>> k8s
['services', 'pods', 'K8s', 'Git', 'openshift']
>>>
```
The best way to remove the last item is to pop. You could use index number to kill the right item in the list
```python
>>> k8s
['services', 'pods', 'K8s', 'Git', 'openshift']
>>> k8s.pop()
'openshift'
>>> k8s    
['services', 'pods', 'K8s', 'Git']
>>>
```
The .remove method can also be used to remove the first occurrence of the item like so:
```python
>>> k8s    
['services', 'pods', 'K8s', 'Git']
>>> k8s.remove('pods') 
>>> k8s
['services', 'K8s', 'Git']
>>>
```


## Using a for loop within a list to simplify and clean code:

```python
>>> squares=[]
>>> for i in range(10):
...     squared=i*i
...     squares.append(squared)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Take a look at this code and how this can be simplified as shown below:
```python
>>> squares = [i*i for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
Note that the functionality of the inner block is put first, followed by the for statement. You can also add conditionals to list comprehensions like below:
```python
>>> squares=[i*i for i in range(10) if i%2==0]
>>> squares
[0, 4, 16, 36, 64]
```
## Strings
String constructor can be used to make strings of other objects like lists as shown below:
```python
>>> my_list = list()
>>> str(my_list)
'[]'
```

It is relatively common for user text to have trailing or leading whitespace. If someone types " yes " in a form instead of “yes” you usually want to treat them the same. Python strings have a strip method just for this case
```python
>>> input = "  I want more  "
>>> input.strip()
'I want more'
>>> input.rstrip()
'  I want more'
>>> input.lstrip()
'I want more  '
```

On the other hand, if you want to add padding to a string, you can use the ljust or rjust methods. Either one pads with whitespace by default, or takes a character argument:
```python
>>> output = 'Barry'
>>> output.ljust(10)
'Barry     '
>>> output.rjust(10, '*')
'*****Barry'
 ```
 
 ## Splitting strings
 Let's just say you wanna "split" a sentence into words. Use this. Here we goo:
```python
>>> text = "Mary had a little lamb"
>>> text.split()
['Mary', 'had', 'a', 'little', 'lamb']
>>> url = "gt.motomomo.io/v2/api/asset/143"
>>> url.split('/')
['gt.motomomo.io', 'v2', 'api', 'asset', '143']
```

## Joining strings

You can easily create a new string from a sequence of strings and join
them into a single string. This method inserts a string as a separator
between a list of other strings:
```python
>>> items = ['cow', 'milk', 'bread', 'butter']
>>> " and ".join(items)
'cow and milk and bread and butter'
```
There are other methods to capitalize and lower case a string. Those are easily available on google dude. Not gonna cover those
Here are some commonly used python methods
```python
>>> "William".startswith('W')
True
>>> "William".startswith('Bill')
False
>>> "Molly".endswith('olly')
True
>>> "abc123".isalnum()
True
>>> "abc123".isalpha()
False
>>> "abc".isalnum()
True
>>> "123".isnumeric()
True
>>> "Sandy".istitle()
True
>>> "Sandy".islower()
False
```
## Formatting strings in Python

Using curly brackets in the string to indicate replacement fields like so:
```python
>>> '{} come before {}'.format('first','second')
'first come before second'
```

You can specify index numbers in the brackets to insert values in a different order as desired. Which allows you to repeat a value as well. Like so:
```python
'{1} comes after two but {0} does not come after two'.format('one','three') 
'three comes after two but one does not come after two'
```
An even more powerful feature is that the insert values can be specified by a name or a key like so:
```python
'{country} is an island {country} is off the coast of {continent} in the {ocean}'.format(country='Madagascar', continent='Africa', ocean='Indian Ocean')
'Madagascar is an island Madagascar is off the coast of Africa in the Indian Ocean'
```
You can also use a dictionary to replace the values in a string like so:
```python
>>> values={'firstName':'Bill', 'lastName':'Cosby'} 
>>> "Won\'t you come to school {firstName} {lastName}".format(**values) 
"Won't you come to school Bill Cosby"
```

You can also specify format specification arguments. Here below we will add left and right padding using < and >

```python
>>> text="{0:>22}||{0:<22}"
>>> text.format('P','P') 
'                     P||P                     '
>>> text="{0:<>22}||{0:><22}"
>>> text.format('Q','Q') 
'<<<<<<<<<<<<<<<<<<<<<Q||Q>>>>>>>>>>>>>>>>>>>>>'
```

### F-strings in Python
These are more straightforward compare to the format method. f-strings are prepended with either f or F before the first quotation mark. 
- f-strings use curly braces to mark the replacement fields. In an f-string however, the content of the replacement field is an expression.
- This approach could mean you could even do some sort of calculations. let's see below:
