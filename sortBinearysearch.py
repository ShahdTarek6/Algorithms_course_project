def pair_sum_array(X, target_sum):
    X.sort()
    n = len(X)
    for i in range(n):
        k = binary_search(X, 0, n - 1, target_sum - X[i])
        if k >= 0:
            return True
    return False

def binary_search(X, l, r, key):
    while l <= r:
        mid = l + (r - l) // 2
        if X[mid] == key:
            return mid
        elif X[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Example usage:
X = [1, 7, 4, 15, 10]
target_sum = 17
result = pair_sum_array(X, target_sum)
print(result)
