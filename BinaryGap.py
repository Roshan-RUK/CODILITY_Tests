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