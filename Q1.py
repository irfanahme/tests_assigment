def find_sums(n):
    fact = 1
    num = []
    sums = 0
    for i in range(1,n+1):
        fact*=i
    num=map(int, str(fact))
    for i in num:
        sums+=i
    return sums
print(find_sums(100))
