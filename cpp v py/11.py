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
    if arr[i]==0:
        mins = arr[i];
        sums = 0
    else:
        sums += arr[i]
print("Сумма: ", sums)
for i in range(n):
    for j in range(n):
        if arr[i]<arr[j]:
            b=arr[j]
            arr[j]=arr[i];
            arr[i]=b;
print(arr)
