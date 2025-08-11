def addone (x):
    x=x+1
    print ("inside function: ",x)
    x=5 
    addone (x)
    print ("outside function:" ,x)
    def modifylist (lst):
        lst.append(4)
        print ("inside function :",lst)
        lst = [1,2,3]
        modifylist(list)
        print("outside function :",lst)
        lst = [1,2,3]
        modifylist(lst)
        print("outside function :",lst)
        



