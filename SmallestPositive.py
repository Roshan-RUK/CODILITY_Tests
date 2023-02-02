#Find the smallest positive integer not present in the list
#Eg: Givem : A = [11, 2, 6, 4, 3, 1] O/P: 5
#Given : A = [-1,-2,-3] O/P: 1
def solution(A):
    flag = False
    B = []
    for i in range(0,len(A)): #To get list of all Positive numbers > 0
        if A[i] > 0:
            B.append(A[i])
            flag = True
    B= sorted(B)
    count = 0
    smallPos = 1
    maxLimit = len(B)
    for count in range(1,maxLimit):
        if flag == True:
            if count not in B:
                smallPos = count
                break
            elif count == maxLimit:
                smallPos = count + 1
            else:
                smallPos = 1
                count = count + 1
    if count == maxLimit:
        smallPos = count +1
    return smallPos

A = [11, 2, 6, 4, 3, 1]
#A = [1,2,3]
#A = [-1,-2,-3]
solution(A)
found = solution(A)
print(found)