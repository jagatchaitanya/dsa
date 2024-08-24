def primeinrange(min_number,max_number):
    k = int(max_number ** 0.5)+1
    numbersinrange = set(range(min_number,max_number+1))
    for i in range(2,k):
        j = 2
        while i*j<=max_number:
            numbersinrange.discard(i*j)
            j=j+1
    return numbersinrange

print(primeinrange(2,20))
