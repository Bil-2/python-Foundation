n = int (input ("enter n:"))
sum = 0
for i in range (1,n+1):
    sum+= i
    print ("sum of all number till n is ", sum)
    n1 = int (input ("enter another n :"))
    sum1 = 0
    for i in range (1,n1 +1):
        sum1 += i 
        print ("sum of all number till n is ",sum1)