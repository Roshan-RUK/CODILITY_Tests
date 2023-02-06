#Max rotation of table to find dish for individual
#Eg A = [1, 3, 5, 2, 8, 7, 4], B = [7, 1, 9, 8, 5, 7, 4] O/P = 2
def solution(A, B):
    rotation = 0
    max_counter = 0
    for i in range(1,len(A)+1):
        for k in range(0,len(A)):
            if A[k] != B[k]:
                max_counter = max_counter +1
                continue
            else:
                rotation = rotation + 1
                break
        if rotation == len(A):
            rotation= -1
        elif rotation == 0:
            rotation = 0
        if max_counter >= len(A):
            break
        B = B[-1:] + B[:-1]
    return rotation

#A = [1, 1, 1, 1]
#B = [1, 1, 1, 1]
#A = [3, 5, 0, 2, 4]
#B = [1, 3, 10, 6, 7]
#A = [1, 1, 1, 1]
#B = [1, 2, 3, 4]
A = [1, 3, 5, 2, 8, 7, 4]
B = [7, 1, 9, 8, 5, 7, 4]
rotate= solution(A, B)
print(rotate)