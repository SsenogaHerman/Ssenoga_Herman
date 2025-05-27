class Person:
     def __init__(self,first_name,last_name,age):
         self.first_name=first_name
         self.last_name=last_name
         self.age=age
     
     def display_info(self):       #Method displays all object attributes
         print(f"First Name:{self.first_name}")
         print(f"Last Name:{self.last_name}")
         print(f"Age:{self.age}")
         
class Student(Person):
    def __init__(self, first_name, last_name, age,reg_number,course):
        super().__init__(first_name, last_name, age)  
        self.reg_number=reg_number
        self.course=course
    
    def display_info(self):
        super().display_info() 
        print(f"Registration NUmber:{self.reg_number}")
        print(f"Course:{self.course}") 
        print("____________________")         
        
        
class Lecturer(Person):
    def __init__(self, first_name, last_name, age,ID,title):
        super().__init__(first_name, last_name, age)  
        self.ID=ID
        self.title=title
    
    def display_info(self):
        super().display_info() 
        print(f"ID:{self.ID}")
        print(f"Title:{self.title}") 
        print("____________________") 
        
class Staff(Person):
    def __init__(self, first_name, last_name, age,ID,role):
        super().__init__(first_name, last_name, age)  
        self.ID=ID
        self.role=role
    
    def display_info(self):       
        super().display_info() 
        print(f"Staff ID:{self.ID}")
        print(f"Role:{self.role}")                        
        print("____________________")
         

student=Student("Herman","Ssenoga",22,"23/U/17648","Bachelor of Science In Software Engineering")
student.display_info()

lecturer=Lecturer("John","Davis",33,"L-045","Professor")
lecturer.display_info()

staff=Staff("Museveni","Tihaburwa",65,"S-120","Librarian")   
staff.display_info()   
