class superclass:
    name=""
    marks=0.0
    def sdisplay(self):
        print"satya")
class subclass(superclass):
    def fdisplay(self):
        self.name="vamsikumar"
        self.marks=428
        print("my name is",self.name,"my results:",self.marks)
object=subclass()
object.sdisplay()
object.fdisplay()
#singe inheritance
class parent():
    resut=''
    grade=''
    def dispay(self):
        print("HI HOW ARE YOU?")
class chid(parent):
    def show(self):
        self.resut='PASS'
        self.grade='B'
        print("MY MARKS IS:",self.resut,'my grade is:',self.grade)
p1=chid()
p1.dispay()
p1.show()
        
class akshmi():
    food=''
    drinks=''
    tota_cost=0.0
    def dispay(self):
        print('wecome to singe inheritance!')
class sweety(akshmi):
    def show(self):
        self.food='biryani'
        self.drinks='thumsup'
        tota_cost=200
        print('THIS IS SO YUMMY!', self.food,"nice drink:",self.drinks)
p2=sweety()
p2.dispay()
p2.show()


class base():
    def dispay(self):
        print("HII SINGE INHERITANCE!")
        
class derived(base):
    def show(self):
        print("HII HOW ARE YOU?")
x=derived()
x.dispay()
x.show()

'''class parent():
    def __init__(self):
        self.name=name
        self.id=id
        print('HII')
    def empoy_detaie(self):
        return  self.id, self.name
    def empoy_check(self):
        if self.id == 5000:
            print("this is vaid id")
        else:
            print("this is not vaid id")
class chid(parent):
    def end(self):
        print("PROGRAM WI BE ENDED")
p1=parent('RAVI','689353')        
object=chid()
object.empoy_detaie()
object.empoy_check()'''
        
'''class Parent_class(object):
    def __init__(self, name, id): 
        self.name = name 
        self.id = id
    def Employee_Details(self): 
        return self.id , self.name
    def Employee_check(self): 
        if self.id > 500000:
           return " Valid Employee "
        else:
           return " Invalid Employee "
class Child_class(Parent_class): 
    def End(self):
        print( " END OF PROGRAM " ) 
Employee1 = Parent_class( "Employee1" , 600445)  # parent class object
print( Employee1.Employee_Details() , Employee1.Employee_check() ) 
Employee2 = Child_class( "Employee2" , 198754) # child class object 
print( Employee2.Employee_Details() , Employee2.Employee_check() ) 
Employee2.End()'''

'''class fun():
    vaue1=0.0
    vaue2=0.0
    def __init__(self,vaue1,vaue2):
        self.vaue1=vaue1
        self.vaue2=vaue2
        print('HIIIIIII')
    def add(self):
        print('vaue1:',self.vaue1)
        print('vaue2:',self.vaue2)
        return self.vaue1+self.vaue2
    def mutipe(self):
        print('vaue1:',self.vaue1)
        print('vaue2:',self.vaue2)
        return self.vaue1*self.vaue2
    def div(self):
        print('vaue1:',self.vaue1)
        print('vaue2:',self.vaue2)
        return self.vaue1-self.vaue2

class sum(fun):
    pass
object=sum(30,50)
print(object.add)
object2=sum(20,40)
print(object.mutipe)
print(object.add())
print(object.mutipe())
print(object.div())'''



































