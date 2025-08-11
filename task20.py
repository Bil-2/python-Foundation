num = int (input ("positive number "))
if num % 15 == 0 : 
    print ("number diviisible by 15")
else:
    if num % 3 == 0 or num % 5 == 0:
        print (" number not divisible by 15 but divisible  by 3 or 5 ")
    else :
        print ("number is neither divisible by 3 or by 5  ")

