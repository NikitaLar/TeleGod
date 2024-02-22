f=open('example.txt',"w+" and 'r+')
day=0

g=f.readlines()
d={}

for i in g:
    k=0
    for s in i:
        k=k+1
        if s=="|":
            break
    day=i[:k-1]
    tema=i[k:-1]
    d[day]=tema

#print(d)

today=int(day)+1
print("сегодня", today,"день обучения")
rep=[]
if today>=121:
    rep1=str(today-120)
    rep.append(d[rep1])
if today>=8:
    rep2=str(today-7)
    rep.append(d[rep2])
if today>=6:
    rep3=str(today-5)
    rep.append(d[rep3])
if today>=2:
    rep4=str(today-1)
    rep.append(d[rep4])
else:
    rep.append("нет")

#print(rep)

print(" ")
print("темы для повторения:")
for o in rep:
    print(o)

print(" ")
print("сегодняшняя новая тема ( ↓ Введите Ниже ↓ )")
tema=input()
today=str(today)
f.write(today+"|"+tema+"\n")

print("УСПЕШНО")