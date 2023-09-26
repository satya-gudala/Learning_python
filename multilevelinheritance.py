#Multilevel Inheritance Works in Python?......1 grand base cass,parent-(base,derived,),chid-derivedcass
class gparent():
    def gdispay(self):
        print('grandparent')
class parent(gparent):
    def pdispay(self):
        print('parent')
class chid(parent):
    def cdispay(self):
        print('chid')
p1=chid()
p1.gdispay()
p1.pdispay()
p1.cdispay()

class base():
    def bdispay(self):
        print('10')
class base2(base):
    def tdispay(self):
        print ('20')
class derived(base2):
    def ddispay(self):
        print('30')
p=derived()
p.bdispay()
p.tdispay()
p.ddispay()

class famiy():
    def __init__(self,father,chid):
        print('HII')
    def dispay(self):
        print('my famiy')
class father(famiy):
    def fdispay(self):
        self.father=father
        self.chid=chid
        print('my father name:', self.father)
class chid(father):
    def cdispay(self):
        print('my chid name:',self.chid)
p=chid('satya','sweety')
p.dispay()
p.fdispay()
p.cdispay()


#singe inheritance():
class parent():
    def dispay(self):
        print('heo')
        
class chid(parent):
    def show(self):
        print('satya')
z=chid()
z.dispay()
z.show()


'''class satya():
    food=''
    drink=''
    def __init__(self,food,drink):
        self.food=food
        self.drink=drink
        print('skjdnvkuhdiv')
class sweety(satya):
    def show(self):
        print('THIS IS RETURN FUNCTION')
o=sweety('biryani','water')
print(o.show())'''




#mutieve-inheritance():
class grandparent():
    def dispay(self):
        print('SATYA-KRISHNA')
class parent(grandparent):
    def pdispay(self):
        print('VAMSI_KRIUSHNA')
class chid(parent):
    def show(self):
        print('SWEETY_KRISHNA')
v=chid()
v.dispay()
v.pdispay()
v.show()


#hierarchica inheritance():...................................>
class base():
    def satya(self):
        print('hierarchica inheritance:')
class derived1(base):
    def dsatya(self):
        print('1DERIVED CASS INHERITANCE:')
class derived2(derived1):
    def asatya(self):
        print('2DERIVED CASS INHERITANCE:')
object=derived2()
object.satya()
object.dsatya()
object.asatya()

class Detais():
    def __init__(self,id,name,age):
        self.id=''
        self.name=''
        self.age=''
    def setdata(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def datashow(self):
        print("id:",self.id)
        print("name:",self.name)
        print("age:",self.age)
class empoyee(Detais):
    def __init__(self):
        self.company=''
        self.dep=''
    def setempoyee(self,id,name,age,company,dep):
        self.company=company
        self.dep=dep
    def empoyeeshow(self):
        print("company:",self.company)
        print("department:",self.dep)
class doctor(empoyee):
    def __init__(self):
        self.hospita=''
        self.dept=''
    def doctorset(self,id,name,age,hospita,dept):
        self.hospita=hospita
        self.dept=dept
    def showdoctor(self):
        print("hospita:",self.hospita)
        print("department:",self.dept)

print('empoyee:')
b=empoyee()
print(b.setempoyee(1,'ravi','20','tcs','cse'))
b.empoyeeshow()
print('doctor:')
c=doctor()
c.doctorset(2,'satya','19','bvrm','hdgad')
c.showdoctor()

        

#mutipe inheritance():.....................................>
class father():
    fname=''
    def fdispay(self,fname):
        self.fname="MURTHY"
        
        print('MY FATHER NAME IS:', self.fname)
        
class mother():
    def mdispay(self,mname):
        self.mname="BHAGYA"
        print('MY MOTHER NAME IS:', self.mname)
        
class kid(father,mother):
    def cdispay(self):
        print('THIS IS ME YOUR KID')
x=kid()
print(x.fdispay('VAMSI-KUMAR'))
print(x.mdispay('SATYA_VATHI'))
print(x.cdispay())


class parent():
    def satya(self):
        print("hii how are ypu")
class grandparent():
    def sweety(self):
        print('HII! I AM GOOD')
class chid(parent,grandparent):
    def vamsi(self):
        print('wecome')
d=chid()
d.satya()
d.sweety()
d.vamsi








        




        









