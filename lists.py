# LIST LESSON
# List Methods	Description
# append()	    It adds a new element to the end of the list.
# extend()	    It extends a list by adding elements from another list.
# insert()	    It injects a new element at the desired index.
# remove()	    It deletes the desired element from the list.
# pop()	        It removes as well as returns an item from the given position.
# clear()	        It flushes out all elements of a list.
# index()	        It returns the index of an element that matches first.
# count()	        It returns the total no. of elements passed as an argument.
# sort()	        It orders the elements of a list in an ascending manner.
# reverse()	    It inverts the order of the elements in a list.
# copy()	        It performs a shallow copy of the list and returns.

# Function	Description
# all()	    It returns True if the list has elements with a True value or is blank.
# any()	    If any of the members has a True value, then it also returns True.
# enumerate()	It returns a tuple with an index and value of all the list elements.
# len()	    The return value is the size of the list.
# list()	    It converts all iterable objects and returns as a list.
# max()	    The member having the maximum value
# min()	    The member having the minimum value
# sorted()	It returns the sorted copy of the list.
# sum()	    The return value is the aggregate of all elements of a list.


# Create a Python list using subscript operator
# Syntax
# L1 = [] # An empty list
# L2 = [a1, a2,...] # With elements

# blank list
L1 = []

# list of integers
L2 = [10, 20, 30]

# List of heterogenous data types
L3 = [1, "Hello", 3.4]

# Create Python list using list()
# Syntax
# theList = list([n1, n2, ...] or [n1, n2, [x1, x2, ...]])

theList = list() #empty list
len(theList)
# 0

theList = list([1,2])
theList
# [1, 2]

theList = list([1, 2, [1.1, 2.2]])
theList
# [1, 2, [1.1, 2.2]]
len(theList)
# 3

#Syntax - How to use List Comprehension
# theList = [expression(iter) for iter in oldList if filter(iter)]
theList = [iter for iter in range(5)]
print(theList)

listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
firstLetters = [ country[0] for country in listofCountries ]
print(firstLetters)
# ['I', 'A', 'E', 'G', 'B', 'V']

print ([x+y for x in 'get' for y in 'set'])
# ['gs', 'ge', 'gt', 'es', 'ee', 'et', 'ts', 'te', 'tt']

print ([x+y for x in 'get' for y in 'set' if x != 't' and y != 'e' ])
# ['gs', 'gt', 'es', 'et']

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
oddMonths = [iter for index, iter in enumerate(months) if (index%2 == 0)]
oddMonths
# ['jan', 'mar', 'may', 'jul', 'sep', 'nov']

init_list = [0]*3
print(init_list)
# [0, 0, 0]
# two_dim_list = [ [0]*3 ] *3
two_dim_list = [ [0]*3 ] *3
print(two_dim_list)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
two_dim_list[0][2] = 1
print(two_dim_list)
# [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

two_dim_list = [[0]*3 for i in range(3)]
print(two_dim_list)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

two_dim_list[0][2] = 1
print(two_dim_list)
# [[0, 0, 1], [0, 0, 0], [0, 0, 0]]

L1 = ['a', 'b']
L2 = [1, 2]
L3 = ['Learn', 'Python']
L1 + L2 + L3
# ['a', 'b', 1, 2, 'Learn', 'Python']

L1 = ['a', 'b']
L2 = ['c', 'd']
L1.extend(L2)
print(L1)
# ['a', 'b', 'c', 'd']

L1 = ['x', 'y']
L1.append(['a', 'b'])
L1
# ['x', 'y', ['a', 'b']]

vowels = ['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#Accessing list elements using the index operator
print(vowels[0])
print(vowels[2])
print(vowels[4])
#Testing exception if the index is of float type
try:
 vowels[1.0]
except Exception as ex:
 print("Note:", ex)

#Accessing elements from the nested list
alphabets = [vowels, consonants]

print(alphabets[0][2])
print(alphabets[1][2])

# Output
# a
# i
# u
# Note: list indices must be integers or slices, not float
# i
# d
#
# vowels = ['a','e','i','o','u']
print(vowels[-1])
print(vowels[-3])
#The Python slicing operator syntax
# [start(optional):stop(optional):step(optional)]
# Say size => Total no. of elements in the list.
# Start (x) -> It is the point (xth list index) where the slicing begins. (0 =< x < size, By default included in the slice output)
# Stop (y) -> It is the point (y-1 list index) where the slicing ends. (0 < y <= size, The element at the yth index doesn't appear in the slice output)
# Step (s) -> It is the counter by which the index gets incremented to return the next element. The default counter is 1.
# Let’s consider the following list of integers.
theList = [1, 2, 3, 4, 5, 6, 7, 8]
# In the examples to follow, we’ll test various slice operations on this list. You must know that not only we can use a slice operator for slicing but also for reversing and copying a list.

# Slicing lists
# Examples of slicing a list by using indexes.
# Return the three elements, i.e. [3, 4, 5] from the list
theList[2:5]
# [3, 4, 5]
# Since the Python list follows the zero-based index rule, so the first index starts at 0.
# Print slice as [3, 5], Don’t change the first or last index
theList[2:5:2]
# [3, 5]
# In this example, we incremented the step counter by ‘2’ to exclude the median value, i.e., ‘4’ from the slice output.

# Slice from the third index to the second last element
# You can use a negative value for the stop argument. It means the traversing begins from the rearmost index.
# A negative stop value, such as ‘-1’ would mean the same as “length minus one.”
theList[2:-1]
# [3, 4, 5, 6, 7]
# Get the slice from start to the second index
# In slicing, if you don’t mention the “start” point, then it indicates to begin slicing from the 0th index.
theList[:2]
# [1, 2]
# Slice from the second index to the end
# While slicing a list, if the stop value is missing, then it indicates to perform slicing to the end of the list. It saves us from passing the length of the list as the ending index.
theList[2:]
# [3, 4, 5, 6, 7, 8]
# Reverse a list
# It is effortless to achieve this by using a special slice syntax (::-1). But please note that it is more memory intensive than an in-place reversal.
# Reverse a list using the slice operator
# Here, it creates a shallow copy of the Python list, which requires long enough space for holding the whole list.
theList[::-1]
# [8, 7, 6, 5, 4, 3, 2, 1]
# Here, you need a little pause and understand, why is the ‘-1’ after the second colon? It intends to increment the index every time by -1 and directs to traverse in the backward direction.
# Reverse a list but leaving values at odd indices
# Here, you can utilize the concept learned in the previous example.
theList[::-2]
# [8, 6, 4, 2]
# We can skip every second member by setting the iteration to ‘-2’.

# Python Add Two List Elements
# Copy a list
# Let’s see how does slice operator creates a copy of the list.
# Create a shallow copy of the full list
id(theList)
# 55530056
id(theList[::])
# 55463496
# Since all the indices are optional, so we can leave them out. It’ll create a new copy of the sequence.
# Copy of the list containing every other element
theList[::2]
# [1, 3, 5, 7]

# Iterate Python list
# Python provides a traditional for-in loop for iterating the list. The “for” statement makes it super easy to process the elements of a list one by one.
for element in theList:
 print(element)
# If you wish to use both the index and the element, then call the enumerate() function.
for index, element in enumerate(theList):
 print(index, element)
# If you only want the index, then call the range() and len() methods.
for index in range(len(theList)):
 print(index)
# The list elements support the iterator protocol.
# To intentionally create an iterator, call the built-in iter function.
# it = iter(theList)
# element = it.next() # fetch first value
# element = it.next() # fetch second value
# Check out the below example.
theList = ['Python', 'C', 'C++', 'Java', 'CSharp']
for language in theList:
 print("I like", language)
# Output
# I like Python
# I like C
# I like C++
# I like Java
# I like CSharp

# Add elements to a list
# Unlike the string or tuple, the Python list is a mutable object, so the values at each index can be modified.
# You can use the assignment operator (=) to update an element or a range of items.

# Assignment operator
theList = ['Python', 'C', 'C++', 'Java', 'CSharp']
theList[4] = 'Angular'
print(theList)
theList[1:4] = ['Ruby', 'TypeScript', 'JavaScript']
print(theList)
# Output
# ['Python', 'C', 'C++', 'Java', 'Angular']
# ['Python', 'Ruby', 'TypeScript', 'JavaScript', 'Angular']

# List insert() method
# You can also push one item at the target location by calling the insert() method.
theList = [55, 66]
theList.insert(0,33)
print(theList)
# Output
# [33, 55, 66]
# To insert multiple items, you can use the slice assignment.
theList = [55, 66]
theList[2:2] = [77, 88]
print(theList)
# Output
# [55, 66, 77, 88]

# Remove elements from a list
# Python provides various ways to remove or delete elements from a list. Some of these are as follows:

# Del Operator
# You can make use of the ‘del’ keyword to remove one or more items from a list. Moreover, it is also possible to delete the entire list object.
vowels = ['a','e','i','o','u']
# remove one item
del vowels[2]
# Result: ['a', 'e', 'o', 'u']
print(vowels)
# remove multiple items
del vowels[1:3]
# Result: ['a', 'u']
print(vowels)
# remove the entire list
del vowels
# NameError: List not defined
#print(vowels)

# Remove() and POP() methods
# You can call remove() method to delete the given element or the pop() method to take out an item from the desired index.
# The pop() method deletes and sends back the last item in the absence of the index value. That’s how you can define lists as stacks (i.e., FILO – First in, last out model).
vowels = ['a','e','i','o','u']
vowels.remove('a')
# Result: ['e', 'i', 'o', 'u']
print(vowels)
# Result: 'i'
print(vowels.pop(1))
# Result: ['e', 'o', 'u']
print(vowels)
# Result: 'u'
print(vowels.pop())
# Result: ['e', 'o']
print(vowels)
vowels.clear()
# Result: []
print(vowels)

# Slice operator
# Last but not least, you can also remove items by assigning an empty list with a slice of its elements.
vowels = ['a','e','i','o','u']
vowels[2:3] = []
print(vowels)
vowels[2:5] = []
print(vowels)
# Output
# ['a', 'e', 'o', 'u']
# ['a', 'e']

# Searching elements in a list
# Some of the standard searching methods are as follows:

# In operator
# You can use the Python ‘in’ operator to check if an item is present in the list.
# if value in theList:
#     print("list contains", value)
# List index()
# # Using the Python list index() method, you can find out the position of the first matching item.
# loc = theList.index(value)
# # The index method performs a linear search and breaks after locating the first matching item. If the search ends without a result, then it throws a ValueError exception.
# try:
#     loc = theList.index(value)
# except ValueError:
#     loc = -1 # no match
# # If you would like to fetch the index for all matching items, then call index() in a loop by passing two arguments – the value and a starting index.
# loc = -1
# try:
#     while 1:
#         loc = theList.index(value, loc+1)
#         print("match at", loc)
# except ValueError:
#     pass
# Here is a better version of the above code. In this, we wrapped the search logic inside a function and calling it from a loop.
# Example
theList = ['a','e','i','o','u']
def matchall(theList, value, pos=0):
    loc = pos - 1
    try:
        loc = theList.index(value, loc+1)
        yield loc
    except ValueError:
        pass
value = 'i'
for loc in matchall(theList, value):
    print("match at", loc+1, "position.")
# Output
# match at 3 position.
# Python list supports two methods min(List) and max(List).
# You can call them accordingly to find out the element carrying the minimum or the maximum value.
theList = [1, 2, 33, 3, 4]
low = min(theList)
low
# 1
high = max(theList)
high
# 33

# Sorting a list in Python
# List sort() method
# Python list implements the sort() method for ordering (in both ascending and descending order) its elements in place.
theList.sort()
# Please note that in-place sorting algorithms are more efficient as they don’t need temporary variables (such as a new list) to hold the result.
# By default, the function sort() performs sorting in the ascending sequence.
theList = ['a','e','i','o','u']
theList.sort()
print(theList)
# ['a', 'e', 'i', 'o', 'u']
# If you wish to sort in descending order, then refer to the below example.

theList = ['a','e','i','o','u']
theList.sort(reverse=True)
print(theList)
# ['u', 'o', 'i', 'e', 'a']

#Built-in sorted() function
# You can use the built-in sorted() function to return a copy of the list with its elements ordered.
newList = sorted(theList)
# By default, it also sorts in an ascending manner.
theList = ['a','e','i','o','u']
newList = sorted(theList)
print("Original list:", theList, "Memory addr:", id(theList))
print("Copy of the list:", newList, "Memory addr:", id(newList))
# Original list: ['a', 'e', 'i', 'o', 'u'] Memory addr: 55543176
# Copy of the list: ['a', 'e', 'i', 'o', 'u'] Memory addr: 11259528
# You can turn on the “reverse” flag to “True” for enabling the descending order.
theList = ['a','e','i','o','u']
newList = sorted(theList, reverse=True)
print("Original list:", theList, "Memory addr:", id(theList))
print("Copy of the list:", newList, "Memory addr:", id(newList))
# Original list: ['a', 'e', 'i', 'o', 'u'] Memory addr: 56195784
# Copy of the list: ['u', 'o', 'i', 'e', 'a'] Memory addr: 7327368

