#Fibonacci Series using Recursion
def fibo(n):
    if n <=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

n=5
if n <= 0:
    print("Please enter Positive value")
else:
    print("The fibo series is :")
    for i in range(n):
        print(fibo(i))


#Factorial using recursion
def facto(n):
    if n==1:
        return n
    else:
        return n*facto(n-1)

n=5
print(facto(n))

#To print duplicates
l1= [23,65,23,6,90,2,6,8,8]
l2 = []

l3=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print(l3)
print(l2)

#to remove empty tuple
l1= [23,65,(),90,2,6,(),9]
for i in l1:
    if i == ():
        l1.remove(i)
print(l1)
#print odd numbers in list
l1= [23,65,19,90,2,6,8]
for i in l1:
    if i%2 != 0:
        print(i, end="\n")

#print even numbers in list
l1= [23,65,19,90,2,6,8]
for i in l1:
    if i%2 == 0:
        print(i, end="\n")

#smallest number in a list
l1=[3,-4,1,5,7,0]
l1 = sorted(l1)
small = l1[0]
for i in l1:
    if i < small:
        small = i
print(small)


#Sum all elements in the list
l1 = [1,2,3,4,5,6]
sum = 0
for i in l1:
    sum = sum + i
print(sum)


#Reverse a list
l1 = [1,2,3,4,5,6]
print(l1[::-1])
size = len(l1)
l2 =[]
for i in range(1, len(l1)+1):
    l2.append(l1[size-1])
    size = size -1
print(l2)



#Interchange fisrt and last element in a list
b = [1,2,3,4,5,6]
size = len(b)
temp = b[0]
b[0] = b[size-1]
b[size-1] = temp
print(b)

#Program to swap 2 element
l1= [23,65,19,90]
l2=[1,2,3,4,5]
pos1 =2
pos2 = 3
l1[pos1], l2[pos2] = l2[pos2], l1[pos1]
print(l1, end="\n")
print(l2)

#Nested Dictionary structure
dat = {"emp1":{"name":"Roshan","ID":"123"},
       "emp2":{"name":"Khan","ID":"456"}}
print(dat["emp2"]["name"])

#Sort a string in ascensding and decending
str1 = "python"
str2 = ""
str3 = ""
j = 0
for i in str1:
    str1 = sorted(str1)
    str2 = str2 + str1[j]
    str3 = str1[j] + str3
    j +=1
print("Sorted String in ascending "+str2)
print("Sorted String in descending "+str3)

#Print all non repeating characters in a string
str1 = "aabbcdeeffgh"
result = ""
for i in str1:
    count = 0
    for j in str1:
        if i == j:
            count = count + 1
    if count == 1:
        result += i

print("ALl the unique character in a string "+result)


#Remove repeated character from a string
str1 = "aabbcccdefggggg"
str2 = ""
count = 0
result = ""
for i in str1:
    if i not in str2:
        str2 = str2 + i

print("String without repeated characters "+str2)

#Highest frequency character in a string
str1 = "aabbcccdefggggg"
char_freq = {}

for i in str1:
    if i in char_freq:
        char_freq[i] = char_freq[i] +1
    else:
        char_freq[i] = 1
print("this one")
k = max(char_freq, key = char_freq.get)
print(char_freq[k])
print(max(char_freq, key = char_freq.get))


#Delete vowels in a given string
str1 = "String has vowels"
result = ""
for i in str1:
    i = i.lower()
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        i = ''
    result += i
print("String with deleted vowels "+result)

#Convert a given string into upper case
str1 = "UppErCaSe"
result = ""
for i in str1:
    if i.islower():
        i = i.upper()
    result += i
print("Upper case string is "+result)

#Program to replace string space with given character
str1 = "ques ol"
ch = 's'
result = ""
for i in str1:
    if i == ' ':
        i = ch
    result = result + i
print("Replaced string "+result)

#Program to check given character vowel or consonant
ch = 'p'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Given character is vowel")
else:
    print("Given character is consonant")

#Check if a string is palindrome or not
str1 = "level"
str2 = ""

for i in str1:
    str2 = i + str2

if str1 == str2:
    print("String is a palindrome")
else:
    print("String is not a palindrome")


#Check if two strings are anagram
str1 = "earth"
str2 = "heart"
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("Strings are Anagram")
    else:
        print("Strings are not anagram")
else:
    print("The strings are not of same size and it is not an anagram")

#Count the occurance of a given character in a string
str1 = "This is a string"
ch = 'i'
count =0
for i in str1:
    if i == ch:
        count += 1
print("{}{}{}{}".format("The number of ",ch," Occurance is ", count))



#Return greatest of 3 numbers using lambda
a,b,c = 32, 41, 11
greatest = lambda a, b, c:a if(a > b and a > c) else (b if(b > c) else c)
print(greatest(a,b,c))

#To print fibonacci series
n1,n2 = 0, 1
count = 0
fiboNumber = 10
nth = 0
if fiboNumber <= 0:
    print("Enter Positive integer")
elif fiboNumber == 0:
    print(n1)
elif fiboNumber == 1:
    print(n1,n2)
elif fiboNumber > 1:
    while count < fiboNumber:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

#to reverse an integer
value = 5647
rev = 0
while value!=0:
    rev = rev*10 + value%10
    value = (value//10)
print(rev)



