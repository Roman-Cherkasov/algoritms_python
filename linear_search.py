def linar_search(A, n, x):
    answer = "NOT-FOUND"
    for i in range(0, n):
        # print(i)
        if A[i] == x:
            answer = i
    return answer

def better_linar_search(A, n, x):
    for i in range(0, n):
        if A[i] == x:
            return i
    else:
        return "NOT-FOUND"

def sentinel_linar_search(A, n, x):
    last = A[n - 1]
    A[n - 1] = x
    i = 0
    while (A[i] != x):
        i += 1
    A[n - 1] = last
    if ((i < n - 1) or (A[n - 1] == x)):
        answer = i
    else:
        answer = "NOT-FOUND"
    return answer

a = [5, 15, 9, 22, 4, 9, 66, 16600, 100, 10]

print(sentinel_linar_search(a, len(a), 66))


