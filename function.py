def demo(a):
    print(a)
demo(2)    
#REQUIRED FUNCTION
def demo(a,b):
    c=a+b
    print(c)
demo(3,6)    
def satya(num1,num2):
    sum=num1*num2
    print(sum)
satya(10,20)    

def str(name):
    print('how are you :',name)
str("SATYA_GUDALA")    
#DEFAULT FUNCTION
def cal(a,b=100):
    x=a+b
    print('sum of:',x)
cal(120)    
#ARBITARY FUNCTION
def satya(*marks):
    print(marks)
    print("your passed the exam!")
satya(10,20,30,40,50)

def demo(*kids):
    print('the youngest kid is:',kids[2])
demo('satya','sweety','vamsi','chinnu')    

def fun(*numbers):
    print('hello:',numbers[3])
fun(10,20,30,40,50,60)    
    
#KEYWORD FUNCTION
def keyword(a,b,c):
    print("hello:",c,"rollno:",b,"gender:",a)
keyword(c='satya',b=524,a='female')

##ADD TWO NUMBERS:
def numbers(num1,num2):
    sum=num1+num2
    print('sum:',sum)
add=numbers(30,40)
print(add)

##SUB TWO NUMBERS
def numbers(num1,num2):
    sub=num1-num2
    print("substraction:",sub)
substraction=numbers(100,60)
print(substraction)
##USED RETURN
def demo(x,y):
    div=x/y
    return div
obj=demo(10,3)
print(obj)

##PYTHON LIBRARIES FUNCTION
import math
s=3
sq=math.sqrt(9)
print(sq)

power=math.pow(10,2)
print(power)


pi=math.cos(60)
print(pi)

## EVEN OR ODD NUMBERS
def numbers(n):
    if n%2==0:
        print("THIS IS EVEN NUMBER")
    else:
        print("THIS IS ODD NUMBER")
obj=numbers(11)
print(obj)

##SWAP CASE
'''var1=int(input("enter the variable1:"))
var2=int(input("enter the variable2:"))
temp=var1
var1=var2
var2=temp
print("the swaping the var1",var1)
print("the swaping the var2",var2)

a=input('enter the a value:')
b=input('enter the b value:')
temp=a
a=b
b=temp
print(a)
print(b)

x=10
y=25
temp=x
x=y
y=temp
print(x)
print(y)'''

##sqrt python for Positive Numbers...............>
'''n=float(input('enter the number:'))
sqrt=n**0.5
print('the sqrt is %0.3f is %0.3f'%(n,sqrt))


number=int(input('enter the number'))
sqrt=number*number
print("the sqrt %0.0f is 0.0f"%(number,sqrt))'''


##sqrt in python for Real or Complex Numbers.......>
'''import cmath
num=1+2j
sqrt=cmath.sqrt(num)
print('the sqrt {0} is{1:0.3f}+{2:0.3f}j'.format(num,sqrt.real,sqrt.imag))'''
import cmath
s=4+3j
sqrt=cmath.sqrt(s)
print('the sqrt {0}is {1:0.3f}+{2:0.3f}j'.format(s,sqrt.real,sqrt.imag))


#Matrix Transpose using Nested Loop .................>
X = [[1, 3], [4,5], [7, 9]]

result = [0, 0, 0], [0, 0, 0]

for i in range (len (X)):

              for j in range (len (X[0])):

                             result [j][i] = X [i][j]

for r in result:

              print (r)



##Arguments............>
def demo(fname,lname):
    print(fname+''+lname)
demo('SATYA','GUDALA')    

def demo(fname):
    print(fname + 'WELCOME')
demo('VAMSI_KUMAR')
demo("SATYA_GUDALA")
demo("CHNINNU_GUDALA")


#Passing a List as an Argument...........>
def fun(food):
    for x in food:
        print(x)
fruites=['apple','banana','mango']
fun(fruites)  

def demo(water):
    for i in water:
        print(i)
drink=['thumsup','pepsee','mazza']
demo(drink)

#Return Values.............>
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def fun(x):
    return 3*x
print(fun(3))


def demo(n):
    return 5*n
print(demo(5))


'''s=5*2
print(s)

x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))


x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))



print('satya',end='\\')
print('sweety',end='\\')'''
























