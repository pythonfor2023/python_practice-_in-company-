#create new class
import random 
import string
import time

basic_salary=890000
class Employe_koch:
    def __init__(self,name,age,gender,area,percentage):
        self.name=name
        self.age=age
        self.gender=gender
        self.area=area
        self.percentage=percentage
    
    def generate_assign_id(self):
        if self.age<=25 and self.age>20 and self.gender=="Male" and self.area=="Banglore" or self.area=="local":
            #generate the emplyeeid based on the condition
            end_char=''.join(random.choices(string.ascii_uppercase+string.digits,k=4)) # radom 4 digit key genarataions
            self.employee_id="EMPN"+end_char
        else:
            end_char=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
            self.employee_id="EMPD"+end_char
        print("The name of the employee:",self.name)
        print("The employee_id:",self.employee_id)
        return 

    def genarate_shift(self): 
        self.generate_assign_id()
        if self.employee_id.startswith("EMPN")=="EMPN": # starts with function
             self.assign="Night"
        else:
            self.assign ="DAY"
        print("The assign_id:",self.assign)
        return 

    def  generate_salary(self):
        self.genarate_shift()
        if self.assign=="Night":
            self.increment=basic_salary+4000
        else:
            self.increment=basic_salary
        print("the increment:",self.increment)
        return 
        
    def display(self):
        print("all the details of the employee:")
        print("Waite......")
        time.sleep(5)
        print("Waite......")
        self.generate_salary()
        return 
while(True):
    age=int(input("Plase enter the age:"))
    name=input("Plase enter the name:")
    gender=input("please enter the gender")
    area=input("please enter the area")
    percentage=input("please enter the percentage:")
    obj=Employe_koch(name=name,age=age,gender=gender,area=area,percentage=percentage)
    obj.display()


            
        

     