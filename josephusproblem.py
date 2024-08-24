def josephus_count(n,k):
    if n == 1:
        return 0
    return (josephus_count(n-1,k) + k ) % n

print(josephus_count(5,3))