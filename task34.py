input_string = input("enter string :")
n= int (input("enter n :"))
alphabers = "qwertyuiopasdfghjklmnbvcxz"
reversed_alphabets = alphabets[::-1] 
dict1 = dict(zip(alphabet,reversed_alphabets ))
prefix =input_string[0:n-1]
suffix =input_string[0:n-1]
mirror = ""
for i in range (0 ,len (suffix)):
    mirror = mirror + dict1[suffix[i]]
    res= prefix + mirror
    print ("the result is :",res)