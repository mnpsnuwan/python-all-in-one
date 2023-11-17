# Run in quadratic time : O(n^2)
# 01
def check1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
# f(n) = n*n =n^2
# O(f(n)) = O(n^2)


# 02
def check2(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)
# f(n) = n*(n + (n-1) + (n-2) + ... + 3 + 2 + 1) = n(n+1)/2 = n^2/2 + n/2
# O(f(n)) = O(n^2)


# 03
def check3(n):
    i = 0
    while i < n:
        j = 0
        while j < 3*n:
            j = j + 1
        j = 0
        while j < 2*n:
            j = j + 1
        i = i + 1
# f(n) = n*(3n + 2n) = 5n^2
# O(f(n)) = O(n^2)

