def LIS(a):
    val = [0]*len(a)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i + 1, len(a)):
            if a[j] > a[i] and val[j] >= val[i]:
                val[i] = val[j] + 1
                
    lis = list()
    m = max(val)
    for i in a:
        if val[a.index(i)] == m:
            lis.append(i)
            m -= 1
    return lis

print(LIS([3, 1, 2, 7, 6, 4, 5]))