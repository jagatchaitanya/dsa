def lcslength(string1, string2, memodict):
    m = len(string1)
    n = len(string2)

    if m == 0 or n == 0:
        return 0
    if (m, n) in memodict:
        return memodict[(m, n)]
    if string1[m-1] == string2[n-1]:
        memodict[(m, n)] = 1 + lcslength(string1[:m-1], string2[:n-1], memodict)
    else:
        memodict[(m, n)] = max(lcslength(string1, string2[:n-1], memodict),
                               lcslength(string1[:m-1], string2, memodict))
    return memodict[(m, n)]

string1 = "jakat1"
string2 = "jagat1"
memodict = {}
print(lcslength(string1, string2, memodict), memodict)



