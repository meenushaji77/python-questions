# 1. Create a list of 5 numbers and print the largest number.

list=[45,23,78,12]
largest=list[0]
for i in range(len(list)):
    if list[i] > largest:
        largest=list[i]
print("largest:",largest)

#2. Write a Python program to remove duplicate elements from a list.

number=[2,5,3,6,3,2]
num=[]
for i in number:
    if i not in num:
        num.append(i)  
print(num)

# # 3. Write a program to reverse a list without using the reverse() method.

numbers=[34,8,1,4,9]
print("reverse:",numbers[::-1])

# #  4 .Create a tuple of 5 elements and print the first and last elements. 
number1=(23,54,67,21)
print(number1[0],number1[-1])

# # 5. Write a Python program to count how many times a particular element appears in a tuple.
number2=(10,20,30,20)
print(number2.count(20))

# # 6. Create two sets and find their union and intersection.
x={2,3,4,5}
y={5,6,7,8}
print(x.union(y))
print(x.intersection(y))

# # 7. Write a Python program to remove duplicate elements from a list using a set.

number3=[2,2,4,6,4,7,8]
result=[]
for i in number3:
    if i not in result:
        result.append(i)
print(result)

# # 8. Create a dictionary containing a student's name, age, and mark. Print each value.
person={"name": "meera", "age": "21", "mark": "98"}
print(person.values())

# # 9. Write a Python program to find the key with the highest value in a dictionary.
students={"meera": "98","manu": "78","manoj":"99"}
result= max(students, key=students.get)
print(result)


 # 10. Write a Python program to count the frequency of each character in a string using a dictionary.
text="meenakshi"
frequency={}
for i in text:
    frequency[i]=frequency.get(i,0)+1
print(frequency)

