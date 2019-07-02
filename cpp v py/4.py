import math
x=float(input("Input -1 < x < 1: "))
znak = -1
s = 0
eps = 0.0001
slag = 1
N = 0
k = 1
if -1<x<1:
    while math.fabs(slag)>eps:
        slag=znak*(math.pow(3,N)*math.pow(x,k))/math.factorial(N)
        k=k+2
        N=N+2
        znak=-znak
        s+=slag
    s=s*-1
    print(round(float(s),4))
    print(round(float(x*math.cos(3*x)),4))
else:
  print("Error!")
