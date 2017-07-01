from MyQueue import QueueQS as qsq
from MyQueue import QueueHeap as qh
import time
import random
rand_arr = random.sample(range(1, 33), 32)
rand_arr.insert(0,0)
print(rand_arr)

x = qsq()
for var in rand_arr:
    x.enqueue(var)
new_arr = []

while(not x.isEmpty()):
    new_arr.append(x.dequeue())
print(new_arr)

y = qh()

for var2 in rand_arr:
    y.enqueue(var2)
new_arr2 = []

while(len(y.arr)!=0):
    new_arr2.append(y.dequeue())
print(new_arr2)

index = 1000
lista = []
while(index<=10000):
    print("INDEX: ",index)
    y = qh()
    eq = 0
    dq = 0
    while(len(lista)<index):
        lista.append(random.randrange(index))

    start_time = int(round(time.time() * 1000))


    while (eq < index or dq < index):
        if (random.random() > 0.5 and eq < index):
            y.enqueue(lista.pop())
            eq = eq + 1
        elif(dq < index):
            y.dequeue()
            dq = dq + 1
    end_time = int(round(time.time() * 1000))
    lista = []
    index = index + 100
    print(end_time-start_time)
index = 1000
lista = []
while(index<=10000):
    print("INDEX:",index)
    y = qsq()
    eq = 0
    dq = 0
    while(len(lista)<index):
        lista.append(random.randrange(index))
    start_time = int(round(time.time() * 1000))
    while (eq < index or dq < index):
        if (random.random() > 0.5 and eq < index):
            y.enqueue(lista.pop())
            eq = eq + 1
        elif(dq < index):
            y.dequeue()
            dq = dq + 1
    end_time = int(round(time.time() * 1000))
    lista = []
    index = index + 100
    print(end_time-start_time)