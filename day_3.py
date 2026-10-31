#30-10-26

# 1. Move zeros to the end
numbers = [0, 5, 0, 3, 8, 0, 2]
result=[]
count=0
for i in numbers:
    if i==0:
        count+=1
    else:
        result.append(i)
for i in range(count):
    result.append(0)

print(result)

# 2.  Find pairs whose sum is 10
numbers = [2, 8, 4, 6, 5, 5, 3, 7]
rslt=[]
for i in range(len(numbers)):
    for j in range(i+1,(len(numbers))):
        if numbers[i]+numbers[j]==10:
            rslt.append((numbers[i],numbers[j]))
print(rslt)

# 3. Sort by second element
data = ((1, 5), (2, 3), (3, 8), (4, 1))
result = sorted(data, key=lambda x: x[1])

print(tuple(result))

# 4. Find repeated elements
numbers = (2, 4, 5, 2, 6, 4, 8, 2, 5)
result=[]
for i in numbers:
    if numbers.count(i)>1:
        if i not in result:
         result.append(i)
print(result)

# 5. Dictionary – Invert dictionary
data = {    "a": 1,   
         "b": 2,    
         "c": 3}
result={}
for key,value in data.items():
    result[value]=key
print(result)

# 6. Group even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result={
    "even":[],
    "odd":[]
}
for i in numbers:
    if i%2==0:
        result["even"].append(i)
    else:
        result["odd"].append(i)
print(result)

