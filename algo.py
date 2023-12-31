def checkPairSum(X, n, targetSum):
    hashTable = set()
    for i in range(n):
        k = targetSum - X[i]
        if k in hashTable:
            return True
        hashTable.add(X[i])
    return False

# Example usage:
X = [1, 2, 3, 4, 5, 6]
n = len(X)
targetSum = 9

result = checkPairSum(X, n, targetSum)

if result:
    print("Pair with the target sum exists.")
else:
    print("Pair with the target sum does not exist.")
