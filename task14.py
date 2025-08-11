cost_price = int (input("cost price:"))
selling_price = int (input("selling price:"))
if selling_price > cost_price:
    profit =selling_price - cost_price 
    print (profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price 
    print ( "loss number is ", loss )
else :
    print ("we have made no profit and nop loss ")