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