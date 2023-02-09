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



