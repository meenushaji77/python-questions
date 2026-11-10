#1.  Create a function func1() such that it can accept a variable number of arguments and print all of them. 
#  Whether you pass two numbers or five, the function should handle them all without error.

def func1(*args):
    print("printing values:")
    for i in args:
        print(i)

func1(20,40,60)
func1(80,100)

#2. Write a function calculation() that accepts two variables and calculates both addition and subtraction.
#  The function must return both results in a single return statement.

def calculation(a,b):
    add = a+b
    sub = a-b
    return add,sub

res=calculation(40,10)
print(res)

#3. Create a function show_employee() that accepts an employee’s name and salary. 
# If the salary is not provided in the function call, the function should automatically assign a default value of 9000.positional rule

def show_employee(name,salary=9000):
    print("name:",name ,"salary:",salary)

show_employee("manu",12000)
show_employee("athira")


#4. Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates the addition of a and b. 
# The outer function should then add 5 to that sum and return the final result.

def outer(a,b):
    def inner(a,b):
        return a+b
    add=inner(a,b)
    return add+5
addition=outer(5,3)
print(addition)

#5. Assign a different name to the function display_student(name, age) 
# and call it using the new name. For example, assign it to a variable called show_student

def display_student(name,age):
    print("name:",name,"age:",age)
show_student=display_student

show_student("meera",21)

#6. Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. 
# Call this function twice: once using positional arguments and once using keyword arguments.

def describe_pet(animal_type,pet_name):
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")

describe_pet("cat","melow") #this is positional argument

describe_pet(pet_name="willie",animal_type="dog") #keyword argument

