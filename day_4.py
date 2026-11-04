# 1.find the cube of elements
list=[1,2,3]
result=[]
a=[]
for i in list:
    result=(i,i**3)
    a.append(result)
print(a)

# 2.count the repaeted number of elements in a list numbers
numbers=[10,20,30,40,50,20]
print(numbers.count(20))

# 3.find the largest in a nested list 
data=((1,2),(10,20),(4,5))
largest=data[0]
for i in data:
    if sum(i)>sum(largest):
        largest=i
print(largest)

# 3.find all elements
a={1,2,3,6}
b={6,8,9}
print(a.union(b))

# 4.group students according to their marks
students={"anu":85,
          "rahul":76,
          "meera":89,
          "arun":45,
          "john":35,
          "sara":75
          }
result={
    "excellent":[],
    "average":[],
    "poor":[]
}
for name,marks in students.items():
    if marks>=80:
        result["excellent"].append(name)
    elif marks>=50:
        result["average"].append(name)
    else:
        result["poor"].append(name)
print(result)

# 5.find elements present in one list but not the other
a=[10,20,30,40,50]
b=[30,40,60,70]
set_a=set(a)
set_b=set(b)
only_a=set(a)-set(b)
only_b=set(b)-set(a)
print("only_a",only_a)
print("only_b",only_b)

#6.reverse every word in a list
word=["python","java","developer","coding"]
result=[]
for i in word:
    result.append(i[::-1])
print(result)