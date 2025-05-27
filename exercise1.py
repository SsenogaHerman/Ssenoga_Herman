from multipledispatch import dispatch


#method overriding
class Order:
    def __init__(self,name,destination):
        self.name=name
        self.destination=destination

        
    def order_info(self):
         print(f"Customer Details:{self.name}")
         print(f"Destination:{self.name}")
         print("You are using faras")
         
class Order_Car(Order):
    def order_info(self):  #overriden method of the parent class
         print("_____Using Faras transport services____")
         print(f"Customer Details:{self.name}")
         print(f"Destination:{self.destination}")
         print("You are using faras Car")  
         print("_____________________________")  
         
class Order_bike(Order):
    def order_info(self): #overriden method of the parent class
         print("_____Using Faras transport services____")
         print(f"Customer Details:{self.name}")
         print(f"Destination:{self.destination}")
         print("You are using faras Bike")
         print("_____________________________")
         
order1=Order_bike("Herman","Makerere")
order1.order_info()   

order2=Order_Car("Herman","Makerere")
order2.order_info()                      
         




#method overloading

print("______MOVIE PAYMENT SYSTEM_______")

@dispatch(str,str,str)
def make_payment(movie_name,bank_account_number,bank_name):
    print(f"Movie title:{movie_name}")
    print(f"Account number:{bank_account_number}")
    print(f"Bank name:{bank_name}")
    print("_______Bank Payment sucessful______")
 
@dispatch(str,str)   
def make_payment(movie_name,mobile_number):       #overloaded method with two parameters
    print(f"Movie title:{movie_name}")
    print(f"Mobile Number:{mobile_number}")
    print("_______Mobile Money Payment sucessful______")    
    
    make_payment("Mad Max","230000808","Centenary")
    
    make_payment("Furiosa","0784737887")
    
    

#Method Resolution Order

class Prey:
    def behaviour(self):
     print("Prey can run")
     
class Predator():
    def behaviour(self):
      print("Predator can hunt")
    
    
class Crocodile(Predator,Prey):
   pass

crocodile1=Crocodile()
crocodile1.behaviour()   #behaviour method from Predator class is called since Predator was inherited first by Crocodile class