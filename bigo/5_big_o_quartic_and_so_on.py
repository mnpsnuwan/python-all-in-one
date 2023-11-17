# Run in power of four time : O(n^4)
# 01
def check1(n):
    i = 0
    while i < 3*n:
        j = 10
        while j <= 50:
            j += 1
        j = 0
        while j < n**3:
            j += 2
        i += 1


# f(n) = 3n*(40 + n^3/2) = 120n + 3n^4/2
# O(f(n)) = O(n^4)


# =========================================
# Finding all subsets of a set - O(2^n)
# Finding all permutation of a string - O(n!)
# Sorting using merge sort - O(nlog(n))
# Iterating over all the cells in a matrix of size n by m - O(nm)



