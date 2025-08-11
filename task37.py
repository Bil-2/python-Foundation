def addallnumbers(*args):
    sum =0 
    for  i in args :
        sum+=i
        return sum 
    output = addallnumbers(1,2,.3,4,5)
    print ("the sum is ", output )