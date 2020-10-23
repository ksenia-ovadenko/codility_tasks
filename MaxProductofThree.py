def solution(A):
    A = sorted(A)
    max_num = A[-3:]
    max_neg_num = A[:3]
    from functools import reduce
    if max_num[-1] <=0:
        return reduce(lambda x, y: x*y, max_num)
    elif max_neg_num[0]*max_neg_num[1] > max_num[0]* max_num[1]:
        return max_neg_num[0]*max_neg_num[1]*max_num[2]
    else:
        return reduce(lambda x, y: x*y, max_num)
