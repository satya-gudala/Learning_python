from abc import ABC,abstractmethod
class Aclass(ABC):#abs class
    @abstractmethod
    def display(self):#abs method
       None
    def show(self):
        None
class Bclass(Aclass):#abs class
    def display(self):#abs method
        print("ABSTRACT METHOD!")
class Cclass(Aclass):#concrete class
    def display(self):
        print("display method")
    def show(self):
        print("show method")
obj=Cclass()
obj.display()
obj.show()


from abc import ABC,abstractmethod
class breakfast(ABC):
    def display(self):
        pass
class lunch(breakfast):
    def display(self):
        print("I LIKE BIRYANI")
class snacks(breakfast):
    def display(self):
        print("I WANT PASTA")
    def show(self):
        print("one more pasta")
class dinner(breakfast):
    def display(self):
        print("i like chicken curry")
    def satya(self):
         print("I LIKE BIRYANI")
        
b=lunch()
b.display()
x=snacks()
x.display()
x.show()
s=dinner()
s.display()
s.satya()

from abc import ABC,abstractmethod
class human(ABC):
    def display(self):
        pass
    def show(self):
        print("i can run")
class animal(human):
    def adisplay(self):
        print("their behaviour is wild")
class birds(human):
    def bdisplay(self):
        print("birds can fly")
b=birds()
b.show()
s=animal()
s.adisplay()
x=birds()
x.bdisplay()


from abc import ABC,abstractmethod
class abstract():
    @abstractmethod
    def satya(self):
        None
    def vamsi(self):
        print("ABSTRACT")
class demo(abstract) :
    def dispay(self):
        print("ABSTARCT METHOD")
    def show(self):
        print("ABSTARCT_CASS")
p=demo()        
p.dispay()
p.show()

from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def noofsides(self):
        None    
class triange(shapes):
    def noofsides(self):
        print('i have 3 sides')
class square(shapes):
    def noofsides(self):
        print('i have 4 sides')
class pentagone(shapes):
    def noofsides(self):
        print('i have 5 sides')
class hexagone(shapes):
    def noofsides(self):
        print("i have 6 sides")

p=triange()
p.noofsides()
p1=square()
p1.noofsides()
p2=pentagone()
p2.noofsides()
p3=hexagone()
p3.noofsides()

from abc import ABC,abstractmethod
class anima(ABC):
    @abstractmethod
    def satya(self):
        pass

class bird(anima):
    def satya(self):
        print('i can fy')
class snake(anima):
    def satya(self):
        print('i move to craw')
class human(anima):
    def satya(self):
        print('i want run')
k=bird()
k.satya()
p=snake()
p.satya()
h=human()
h.satya()


from abc import ABC,abstractmethod
class shopping(ABC):
    @abstractmethod
    def dress(self):
        pass
class CMR(shopping):
    def dress(self):
        print('i ike cmr')
    def sweety(self):
        print('hdfieukfh')
class srinidhi(shopping):
    def dress(self):
        print('i dont ike srinidhi')
class sri(shopping):
    def dress(self):
        print('i want sri dress')
s=CMR()
s.dress()

a=srinidhi()
a.dress()
d=sri()
d.dress()

####Implementation of Abstract through Subclass...........>
class parent():
    def __init__(self):
        None
class chid(parent):
    def geeks(self):
        print('geeksforgeeks')

print(issubclass(chid,parent))
print(isinstance(chid(),parent))





























































