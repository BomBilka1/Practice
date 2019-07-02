print("Задание 1")
i=6
while i>0:
    print("*"*i)
    i-=1

print("Задание 2")

k=input("Введите натуральное число: ")
li = list(k)
m = 9
n = 0
index = 0
while len(list(k)) != n:
    if m > int(li[n]):
        m = int(li[n])
        index = n
    n+=1
print("Мин: ",m)
print("Индекс: ",index+1)
