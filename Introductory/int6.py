__author__ = 'egor'

with open("/home/egor/Загрузки/rosalind_ini6.txt","r") as f:
    line=f.readline().strip()
    words=line.split(' ')

answer={}
for word in words:
    if word in answer:
        answer[word]=answer[word]+1
    else:
        answer[word]=1

for key, value in answer.items():
    print(key+' '+str(value))

