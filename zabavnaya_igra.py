num = list(bin(int(input())))
maxim=0
for i in range (len(num)-2):
    if maxim < int(''.join(num),2):
        maxim=int(''.join(num),2)
    num.insert(2,num.pop())
print(maxim)
