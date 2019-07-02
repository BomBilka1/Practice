import math
xm = int(input("Vvedite znachenie X nach: "))
xk = int(input("Vvedite znachenie X kon: "))
dx = int(input("Vvedite shag dx: "))
r = 2
if dx<=0:
    print("Шаг не может равнятся 0")
    exet = input("Pres ENTER to EXIT")
else:
    print("Tablica funkcii")
    for xn in range(xm,xk+1,dx) :
        if -3>=xn:
            y = (2-0)/(-4+6)
            print("X =",xn ,"Y =",y)
        if xn>=-3 and xn<=-3:
            y = xn*0+0
            print("X =",xn ,"Y =",y)
        if xn>-3 and xn<-1:
            y = -(r+(xn+1)**2)**(1/2) 
            print("X =",xn ,"Y =",y)
        if xn>=-1 and xn<=2:
            y = (4-0)/(4+-6)
            print("X =",xn ,"Y =",y)
        if xn>2:
            y = ((2-0)/(-4+6))*(xn-4)
            print("X =",xn ,"Y =",y)
