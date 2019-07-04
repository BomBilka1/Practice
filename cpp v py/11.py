def sortarr(arr):
    do = []
    ot = []
    rez = []
    for i in arr:
        if i <= 1:
            do.append(i)
        if i >= 1:
            ot.append(i)
    for i in do:
        rez.append(i)
    for i in ot:
        rez.append(i)
    return rez
import math
import random
n=int(input("Введте размерность масива: "))
arr=[]
for i in range(n):
    arr.append(random.randint(-10,10))
print(arr)
kol=0
mins=arr[0]
sums=0
for i in range(n):
    if arr[i]>=0:
        kol+=1
print("Кол-во пол.: ",kol)
for i in range(n):
    if 0 not in arr:
        sums=0
    else:
        
        if arr[i]==0:
            mins = arr[i]
            sums = 0
        else:
            sums += arr[i]
print("Сумма: ", sums)

print(sortarr(arr))


