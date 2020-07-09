def LCS(str1, str2, lcs):
    if len(str1) <= 0 or len(str2) <= 0:
        return lcs
    if str1[0] == str2[0]:
        return LCS(str1[1:], str2[1:], lcs + str1[0])
    else:
        return max(LCS(str1[1:], str2, lcs), LCS(str1, str2[1:], lcs), key=len)


print(LCS('bghacdfe', 'bghadf', ''))