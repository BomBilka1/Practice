words=input()
shif=input()

alf=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_size = len(words)
shif_size = len(shif)

words_code = []
shif_code = []
sum_code = []
shifr = []
for i in range(shif_size):
    shif_code.append(alf.index(shif[i]))
    
for i in range(str_size):
    words_code.append(alf.index(words[i]))

    sum_code.append((words_code[i]+shif_code[i%shif_size])%27)

    shifr.append(alf[sum_code[i]])

shifr = ''.join(shifr)

print(shifr)
    
