#find square root a numbers.(methode:1)
num=4
sq=num**0.5
print("here is your sq.root ans",sq)
#methode;2
import math
num1=3
sq1=math.sqrt(num1)
print(sq1)

#calculate the area of a triangle.
height=5
base=2
area=0.5*height*base
print(area)

#write a python program to solve quadratic equation.
#ax*2+bx+c
import cmath
a=4
b=2
c=6
d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print(root1,root2)

#wite the python to swap the variables. (methode:1)
x=2
y=3
temp=x
x=y
print("the value of x:",x)
y=temp
print("the value of y:",y)
#methode;2
a=1
b=2
a,b=b,a
print("the value of a:",a)
print("the value of b:",b)

# write a python program to genrate a randon number.
import random
num2=random.randint(0,7)
print(num2)

#write a program to convert kilometers to miles.
km=4
miles=0.621371*km
print(miles)

#write a progrom that convert celcius to fahrenheit.
celcius=40
fahrenheit=(celcius*(9/5))+32
print(fahrenheit)

#write a python program to check whether the year is leap year or not.
