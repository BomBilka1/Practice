#Задание 1

import math
a1=int(input('a1: '))
b1=int(input('b1: '))
a2=int(input('a1: '))
b2=int(input('a1: '))
n=(abs(a2-a1))
m=(abs(1+a1*a2))
l=n/m
p=math.tan(l)
if a1==a2:
    print("Две прямые параллельны")

elif a1==-1/a2:
    print("Две прямые перпендикулярны")

elif n/m==1:
    print("Угол 45 градусов")

else:
    print("Угол ",p*180/math.pi," градусов")


#Задание 2
k=int(input("\nВведите четырех значное число: "))
a= k/1000
b=(k%1000)/100
c=(k%100)/10
d=(k%10)
if a<b and b<c and c<d and k<10000 and k>999:
    print("True")
else:
    print("False")
