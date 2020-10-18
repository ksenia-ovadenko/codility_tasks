def solution(A, K):
    import numpy as np
    if len(A) == 0 or K == 0:
        return A
    else:
        A_now = A
        for j in range(K):
            A_new = np.zeros(len(A))
            A_new[0] = A_now[len(A_now) - 1]
            for i in range(1, len(A_new)):
                A_new[i] = A_now[i-1]
            A_now = A_new
            print(A_now)
        return A_new
 
