def solution(X, Y, D):
    Jump = 0
    while X < Y:
        X= X + D
        Jump = Jump + 1
    return Jump



X = 10
Y = 101
D = 30
solution(X, Y, D)