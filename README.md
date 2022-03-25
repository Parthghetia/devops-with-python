## Range

```
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

```
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

```
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
```
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
```
>>> while count < 3:
...     print(f"count is {count}")
...     count +=1
... 
count is 0
count is 1
count is 2
```

It is essential to define a way to stop your loop. Otherwise it would be stuck. You could use a break statement to prevent this like so
```
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

```
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

```
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
```
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
```
>>> my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> my_sequence[2:5]
['c', 'd', 'e']
>>> my_sequence[:5]
['a', 'b', 'c', 'd', 'e']
>>> my_sequence[3:]
['d', 'e', 'f', 'g']
```

Sequences share many operations for getting information about them and their contents:
```
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
```
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
```
>>> devops = ['K8s', 'Git']
>>> devops.append('openshift')
>>> devops
['K8s', 'Git', 'openshift']
```
Contents of one list can be added to another using extend like so:
```
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
The best way to remove the last item is to pop
```
>>> k8s
['services', 'pods', 'K8s', 'Git', 'openshift']
>>> k8s.pop()
'openshift'
>>> k8s    
['services', 'pods', 'K8s', 'Git']
>>>
```


