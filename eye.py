def eye(n):
    x = [[0 for l in range(n)] for k in range(n)]
    for i in range(n):
        x[i][i] = 1
    return x

print(eye(5))
