def linar_search(A, n, x):
    answer = "NOT-FOUND"
    for i in range(0, n):
        # print(i)
        if A[i] == x:
            answer = i
    return answer