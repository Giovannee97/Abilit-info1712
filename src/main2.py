a=[]
print(type(a))
a=[*range(0,20,1)]
print(a)
b=a*2
z=list.count(b,0)
print("tipo di z:", type(z))
print("numero di volte che si presenta 0 in b:",z)

import time
v1=[*range(10000)]
v2=[*range(10000)]
t1=time.perf_counter()
sum1=v1+v2
t2=time.perf_counter()
print("conventional sum:",t2-t1)
t3=time.perf_counter()
v1.extend(v2)
t4=time.perf_counter()
print("append command:",t4-t3)

stack=[*range(5)]
print("originale", stack)

for i in range(5,7):
  stack.append(i)
print("ampliato",stack)
stack.pop(0)
stack.pop()
print("poppato",stack)

t="tupla","tupla","tuuuupla", "l'ho inventato iooo"
print(t)

t1="t","o","rta"
print("fetta di torta:",t1[1])

print("lunghezza del verso:", len(t))

d={1:"my",2:"dude", 3:"I ain't gon lie"}
print(d[3])
d.popitem()
print(d)

number=23
running=True

#while running:
#  guess=int(input("dammi un intero:"))

#  if(guess==number):
#    print("bene! hai indovinato!")
#    running=False
#  elif(guess<number):
#    print("un po' più alto...")
#  else:
#    print("un po' più basso...")

#for i in range(0,10):
#  print(i)

while running:
  s=input("non spegnermi!")
  
  if s=="spegniti":
    break
print("ma perché lo hai fatto?!?!")