def gridpaths_count(m,n):
    if m==1 or n==1:
        return 1
    return gridpaths_count(m-1,n)+gridpaths_count(m,n-1)

m = 4
n = 5
print(gridpaths_count(m,n))