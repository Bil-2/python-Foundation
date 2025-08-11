num1=int (input("enret number 1 :"))
num2=int (input("enret number 2 :"))  
operator = input ("enter operarot : ")
match operator : 
   case "+":
      print ("sum is",num1 +num2)
   case "-":
       print ("difference is",num1 - num2)
   case "*":
      print ("product is",num1 * num2)
   case "/":
       print ("division is",num1 / num2)
   case _ :
      print ("a valid operator")