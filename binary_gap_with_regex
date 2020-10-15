def solution(N):
    import re
    bnr = bin(N)[2:]
    fnd = re.findall('(?<=1)0*(?=1)', bnr)
    if not fnd:
        return 0
    else: 
        return len(max(fnd))
    pass
