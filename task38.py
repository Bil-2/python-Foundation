def studentinfo (**kwargs):
    for x,y in kwargs.items():
        print(x,"is", y)
        studentinfo(name="urvi",age=22 ,city = "delhi")
        studentinfo(name = "rai", age =20 , city = "bangalore")