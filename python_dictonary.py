
# if type(number) !="int":
#     print("plase enter the number:")
# create the  dictionary
# ic={}
# type(dic)
# dict ={"data":[]}
# def  dictionary_function():
#     for i in range(0,n):
#         dict1={}
#         dict1["name"]=name
#         dict1["number"]=number
#         print("the name number added  to the dictionaty:")
#         add_user_det(dict1)

# def add_user_det(dict1):
#     dict[""]

#     userdata = { "data":[]}
userdata={"data":[]}
def fil_userdata(age,name,num,country):
  for i in range(0,n):
    user = {}
    user["name"]=name
    user["age"]=age
    user["country"]=country
    add_user(user)

    def add_user(user):
        userdata["data"].append(user)


n=int(input("Enter the number of emloyee sholud be added to the system:"))
name=str(input("Enter the Name:"))
# if type(name) !="str":
#     print("pplase enter the correct format string only:")
age=int(input("enter the age:"))
country=str(input("Enter the contry:"))
num=int(input("enter the Number:"))
fil_userdata(age,name,num,country)
