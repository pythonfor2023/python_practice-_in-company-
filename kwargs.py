
def myFun(*ks): # non-key word argument
	for key in ks:
		print(key)
		# print(ks)
		print(id(key))
		print(type(key))
myFun("ehdee")

def fun(**kwargs):
    print("displaying key world argumment")
    for key,value in kwargs.items():
        print(type(kwargs))
        print("key, value",key,value)

fun(Key="subbu",simple="simple",parameter="meter")

    # Positional arguments 

def simple_function(name,age):
    print("printing the positional argument:")
    print("the argument")
    print(name,age)

simple_function("subbu","Hegde")

# keyword arguments
def fun(name,age):
    print(name,age)
    # print(key,value)
    print(type(name))

fun(name="ravi",age="34")

def carValue(car_price,milage):
    print(car_price,milage)

carValue(milage=232323)
carValue(car_price=232,milage=90909)




