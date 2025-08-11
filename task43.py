def sum_1_to_N(n):
    if n==1:
        return 1
    ans = n+sum_1_to_N(n-1)
    return ans
n=int(input("enter n :"))
print(sum_1_to_N(n))
