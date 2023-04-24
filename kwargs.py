
# def myFun(ks):
# 	for key in ks:
# 		print(key)
# 		# print(ks)
# 		print(id(key))
# 		print(type(key))

# myFun("ehdee")

def fun(**kwargs):
    print("displaying key world argumment")
    for key,value in kwargs.items():
        print(type(kwargs))
        print("key, value",key,value)

fun(Key="subbu",simple="simple",parameter="meter")




