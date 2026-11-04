# 3/11/26

#1. Create a function that accepts a list and returns a new list without duplicates.
def remove_duplicate(numbers):
    result=[]
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
numbers = [2, 4, 2, 6, 4, 8]
print(remove_duplicate(numbers))

#2. Create a function to find the second-largest number in a list.
def second_largest(numbers):
    largest=numbers[0]
    secondlargest=numbers[0]
    for i in numbers:
        if i > largest:
            secondlargest = largest
            largest=i
        elif i > secondlargest and i != largest:
            secondlargest=i
    return secondlargest
numbers = [10, 25, 8, 40, 30]
print(second_largest(numbers))

#3. Create a function that counts how many times each word appears.
def count(words):
    result={}
    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i]=1
    return result
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(count(words))

#4. Create a function to find common elements between two lists using sets.
def common(a,b):
    set_a=set(a)
    set_b=set(b)
    result=(set_a.intersection(set_b))
    return result
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(common(a,b))

#5.Create a function that converts a list of tuples into a dictionary.
def convert(data):
    result={}
    for i in data:
        result[i[0]]=i[1]
    return result
data = [("name", "Meenu"), ("age", 20), ("place", "Kerala")]
print(convert(data))

#6. Separate Even and Odd Numbers
def evenodd(numbers):
    even=[]
    odd=[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        else:
           odd.append(i)
    return even,odd
numbers = [1, 2, 3, 4, 5, 6]
print(evenodd(numbers))

#7. Merge Two Dictionaries
def merge(a,b):
    result={}
    for i in a:
        result[i]=a[i]
    for i in b:
        if i in result:
            result[i]+=b[i]
        else:
            result[i]=b[i]
    return result
a = {"apple": 10, "banana": 20}
b = {"apple": 15, "orange": 30}
print(merge(a,b))

# 8.find the common elements from a set
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
result=[]
for i in a:
    if i in b and i not in result:
        result.append(i)
print(result)

# 9.find the missing number
numbers=[1,2,4,5,7,8,9,10]
for i in range(1,11):
    if i not in numbers:
        print(i)

# 10.rotate the numbers from last by two positions
num=[1,2,3,4,5,6]
for i in range(2):
    last=num.pop()
    num.insert(0,last)
print(num)


