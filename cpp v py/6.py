import math
n=0
e=0.0001
a=2
an=1
while abs(an-a)>=e:
    an=a
    n +=1
    a=((2*n)-1)/(pow(2,n))
print("an= ",an)
print("an-1= ",a)
print("n= ",n)
