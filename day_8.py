#1. Create a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")

#2. Define a global variable global_var = 10. Write a function that successfully changes the value of this global variable to 20.
global_var = 10

def modify_variable():
    global global_var  

    global_var = 20

print("Initial:", global_var)
modify_variable()
print("Modified:", global_var)

#3. Use the filter() function combined with a lambda to extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
numbers=[1,2,3,4,5,6,7,8,9,10]

even=list(filter(lambda x: x%2==0,numbers))
print(even)

#4.a list of tuples representing students and their grades: [("Alice", 88), ("Bob", 75), ("Charlie", 92)].
#  Use the sorted() function and a lambda to sort this list based on the grades (the second element) in ascending order.
students=[("alice",88),("bob",75),("charile",92)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


