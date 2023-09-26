class encap:
    a=10;
    def display(self):
        print("welcome")
obj=encap()
print(obj.a)
obj.display()

class encap:
    a=1000;
    def demo(self):
        print("satyagudala")
obj=encap()
obj.demo()
print(obj.a)

class encap:
    __x=1000;#private variable
    def display(self):
        print("ENCAPSULATION")
        print(self.__x)
object=encap()
object.display()


class encap:
    __x=273846;#private variable
    def __display(self):#private method
        print("ENCAPSULATION PYTHON")
        print(self.__x)
s=encap()
class Car:
    color = "red"
    
    def start(self):
        print("Car started!")
#Implement Encapsulation with a Class in Python
class student():
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank
    def demo(self):
        print("i am:"+ self.name)
        print("i got rank:", self.rank)
obj1=student("satya",1)
obj2=student("sweety",2)
obj1.demo()
obj2.demo()

class demo():
    def __init__(self,name,company,saary):
        self.name=name
        self.company=company
        self.saary=saary
    def empoyee(self):
        print("i am"+self.name)
        print("my company name is:"+self.company)
    def show(self):
        print("my saary is:", self.saary)
str1=demo("SATYA_VATHI",'TCS','20000')
str2=demo("SWEETY_KRISGHNA",'WIPRO','35000')
str1.empoyee()
str2.empoyee()
str1.show()
str2.show()

########Public Member................>
class demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('my name is:'+self.name)
        print('my age is:',self.age)
obj=demo('vamsi',78)
obj.show()

#####Encapsulation in Python using private members.................>
'''class rectange():
    __length=0  #private variable
    __bredth=0      #private variable
    def __iniit__(self):
        self.__length=5
        self.__bredth=3
    def show(self):
        print(self.__length)
        print(self.__bredth)
demo=rectange()
print(demo.__length())
print(demo.__bredth())
demo.show()

class Rectangle:
  __length = 0 #private variable
  __breadth = 0#private variable
  def __init__(self): 
    #constructor
    self.__length = 5
    self.__breadth = 3
    #printing values of the private variable within the class
    print(self.__length)
    print(self.__breadth)
 
rect = Rectangle() #object created 
#printing values of the private variable outside the class 
print(rect.length)
print(rect.breadth)'''

class fun():
    __name=''
    __age=0
    def __init__(self):
        self.__name='chinnu'
        self.__age=15
    def show(self):
        print('my name is:'+ self.__name)
        print('my age is:',self.__age)
p1=fun()
print(p1.show())
        
class employee():
    _name=''
    _saary=0
    _company=""
    def __init__(self,name,saary,company):
        self._name=name
        self._saary=saary
        self._company=company
class display(employee):
    def show(self):
        print('my brother name is:'+ self._name)
        print('my brother saary is',self._saary)
        print('my company name is:'+ self._company)
p2= employee('VAMSI','200','O9')
p3=display('satya','400','xyz')
p3.show()

class food():
    _biryani=''
    _water=''
    _amount=0
    def __init__(self,biryani,water,amount):
        self.biryani=biryani
        self.water=water
        self.amount=amount
        
class show(food):
    def display(self):
        print('my fav food is:'+self.biryani)
        print('my fav drink is:'+ self.water)
p4=food('biryani','7up','300')
p5=show('chicken','thumsup','43')
p5.display()

class demo():
    def __init__(self,name,rono):
        self.__name=name
        self.__rono=rono
    def show(self):
        print(self.__name)
        print(self.__rono)
        
obj1=demo('ravi','525')
obj1.show()

'''class Demo:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(self.__name)
        print(self.__age)

obj1 = Demo('ravi', 20)
obj1.show()'''
########Encapsulation in Python using protected members.............>
class fun():
    _fname='satya'
    _name='sweety'
class show(fun) :
    def __init__(self):
        print(self._fname)
        print(self._name)
k=show()

'''class details:
    _name="Jason"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
# creating object of the class 
obj = pro_mod()'''


































        
