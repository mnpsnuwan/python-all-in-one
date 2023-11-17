# Run in logarithmic time : O(log(n))
# 01 Binary Search
def search_value(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)/2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
    return -1  # val not found
# f(n) = Total comparisons/Total number of cases
# f(n) = (1*(elements requiring 1 comparisons) + 2*(elements requiring 2 comparisons)
#        + . . . + log(n)*(elements requiring logN comparisons))/Total number of cases
# f(n) = (1*1 + 2*2 + 3*4 + . . . + log(n) * (2^log(n-1)))/n+1
# f(n) = (2^log(n)*(log(n-1)) + 1)/n+1
# f(n) = n*(log(n-1))/n+1 + 1/n+1
# O(f(n)) = O(log(n))



