import copy
def replace(index,answer):
      temp=answer[-1]
      for i in range(len(answer)-1,index,-1):
            answer[i]=answer[i-1]
      answer[index]=temp
      index+=1
      return index,answer

def delete(inputKey):
      answer=[]
      for element in inputKey:
            if element not in answer:
                  answer.append(element)
      return answer
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
InputStr=input()
inputKey=input()
shift=int(input())
index=0
answer=delete(inputKey)


for i in range(26):
      if letters[i] not in inputKey and len(answer) < 26 - shift:
            answer.append(letters[i])
      elif letters[i] not in inputKey and len(answer) >=len(letters)-shift:
                  answer.append(letters[i])
                  index, answer=replace(index,answer)
for i in range(len(InputStr)):
      for j in range(len(letters)):
            if InputStr[i]==letters[j]:
                  print(answer[j],end = '')
