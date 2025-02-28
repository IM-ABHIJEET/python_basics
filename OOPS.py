"""
class--------------->
 blueprint for creating the object 

 Object ------------------->
     instance of a class is object 
"""
class Student:
  name="karan"

s1=Student() # object is being created
print(s1.name)

#__________________________________________________________________________________#

""" Constructor-------------->
          it is a function (__init__) which is always invoked while creating an Object
          Consturctor  is of two type------>
          1> Default Construtor
          2> Parameterized Constructor          
"""

class Student:
  def __init__(self):  #Default constructor
    #statemment
     pass
   

  def __init__(self,fullname):
    self.name=fullname
    print("Parameterized constructor:")

s1=Student("Abhijeet")
print(s1.name)

s1=Student("adfsdg")
print(s1.name)

s1=Student("Abhay")
print(s1.name)

#___________________________________________________________________________#


















    


