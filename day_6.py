#find the largest amoung three numbers
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(largest(25,76,43))

#check prime number
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(is_prime(5))
print(is_prime(10))

#reverse a string
def reverse_string(word):
    result=""
    for char in word:
        result=char+result
    return result
print(reverse_string("python"))

#count positive and negative numbers
def count_numbers(numbers):
    positive=0
    negative=0
    for num in numbers:
        if num>0:
            positive+=1
        elif num<0:
            negative+=1
    print("positive numbers :",positive)
    print("negative numbers :",negative)
count_numbers([2,9,-4,10,5,-3,-5,-8])

#remove duplicates from list
def remove(numbers):
    result=[]
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
print(remove([1,2,3,2,4,5,4,6,1,5]))

#simple calculator using function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("addition",add(20,5))
print("substraction",subtract(20,5))
print("multipllication",multiply(20,5))
print("division",divide(20,5))

#create a class with a private variable
class Student:
    def __init__(self):
        self.__name="arun"
    def display_name(self):
        print("student name:",self.__name)
student1=Student()
student1.display_name()
        
#bank account class
class Bank_acconut:
    def __init__(self,name,number,balance):
        self.account_name=name
        self.account_number=number
        self.account_balance=balance
    def display_details(self):
        print("account holder :",self.__account_name)
        print("account balance :",self.__account_balance)
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount deposited :",amount)
        else:
            print("invalid deposite amount")
    def withdraw(self,amount):
        if amount<=0:
            print("invalid deposite amount")
        elif amount>=self.__account_balance:
            self.__account_balance-=amount
            print("amount withdrawn :",amount)
        else:
            print("insuffient balance")
account=Bank_account=("arun",12345,50000)
account.display_details()
account.deposit(5000)
account.withdraw(2000)
account.display_details()