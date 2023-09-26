class moverload():
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
obj.display()
obj.display(10)
obj.display(10,30)
class function():
    def satya(self,x=0,y=0):
        print(x,y)
p1=function()
p1.satya(2)
p1.satya(10,20)
p1.satya(10,28)

def demo(a,b):
    print(a/b)
r=demo(2,6)
print(r)

def show(a,b,c):
    d=a*b+c
    print(d)
show(2,3,4)    
