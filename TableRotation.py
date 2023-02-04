#Code to find longest sequence of zeros in binary representation of an integer.
#Eg: 1041 = 10000010001 O/P : 5
def solution(N):
    binary = bin(N).replace("0b", "")
    max_count = []
    count = 0
    for i in binary:
        if i == '0':
            count = count + 1
        else:
            max_count.append(count)
            count = 0
    return max(max_count)

N = 1041
value = solution(N)
print(value)