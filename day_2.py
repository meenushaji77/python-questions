# 28/10/2026

# 1.Move all zeros to the end
numbers = [0, 5, 0, 3, 8, 0, 2, 7]
num=[]
for i in numbers:
    if i!=0:
        num.append(i)
for x in numbers:
    if x==0:
         num.append(x)
print(num)

# 2. Find the missing number

numbers = [1, 2, 4, 5, 6, 7, 8]
for i in range(len(numbers)):
    if i not in numbers:
        print(i)
    


# # 3. Find duplicate elements
numbers = [2, 5, 3, 2, 8, 5, 9, 3, 3]
result=[]
duplicate=[]
for i in numbers:
    if i not in result:
        result.append(i)
    else:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)

# # 4. Rotate a list to the right
numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])


# # 5. Find common elements in three lists
A = [1, 2, 3, 4, 5, 6]
B = [2, 4, 6, 8, 10]
C = [0, 2, 4, 6, 12]
result=set(A)&set(B)&set(C)
print(result)

# # 6. Merge two dictionaries and add common values

stock1 = {"apple": 10, "banana": 5, "orange": 8}
stock2 = {"apple": 4, "banana": 7, "grape": 6}
rslt= stock1.copy()
for item,quantity in stock2.items():
    if item in result:
        rslt[item]+=quantity
    else:
        rslt[item] = quantity  
print(rslt)

# # 7.Group words by their first letter
words = ["apple", "ant", "ball", "bat", "cat", "car", "axe"]
result={}
for word in words:
    first=word[0]

    if first not in result:
        result[first]=[]
    result[first].append(word)
print(result)


# # 8.#print list in descenting and ascending order
numbers=[3,1,4,2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# #9.find sum of numbers in a tuple
numbers=(3,7,5,8)
sum=0
for i in numbers:
    sum+=i
print(sum)

# # 10.find the product of numbers
numbers=[2,4,6,8]
result=[]
for i in range(len(numbers)):
    product=1
    for j in range(len(numbers)):
        if j != i:
            product*=numbers[j]
    result.append(product)
print(result)





