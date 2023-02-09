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



