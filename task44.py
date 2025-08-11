def power_a_b(a,b):
    if b==0:
        return 1
    ans = a*power_a_b(a,b-1)
    return ans
a= int (input("enter a:"))
b = int (input("enter b:"))
print(power_a_b(a,b))