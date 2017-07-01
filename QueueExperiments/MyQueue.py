import math
class QueueQS:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return self.arr == []

    def enqueue(self, elem):
        self.arr.append(elem)
        QueueQS.__qsort(self,self.arr)

    def dequeue(self):
        if(self.isEmpty()):
            return None
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def __part(self,a, p, r):
        k = a[r]  # pivot
        j, q = p, p
        if p < r:
            for i in range(p, r + 1):
                if a[i] <= k:
                    t = a[q]
                    a[q] = a[j]
                    a[j] = t
                    if i != r:
                        q += 1
                    j += 1
                else:
                    j += 1
            QueueQS.__part(self,a, p, q - 1)
            QueueQS.__part(self,a, q + 1, r)
        return a

    def __qsort(self,a):
        if len(a) > 1:
            r= len(a)-1
            return QueueQS.__part(self, a, 0, r)
        else:
            return a

class QueueHeap:
    def __init__(self):
        self.arr = []



    def isEmpty(self):
        return self.arr == []

    def enqueue(self, elem):
        self.arr.append(elem)
        QueueHeap.__upheap(self,len(self.arr)-1)





    def dequeue(self):

        if(self.isEmpty()):
            return None
        if(len(self.arr) is 1):
            return self.arr.pop()
        else:
            temp = self.arr[len(self.arr)-1]
            deq = self.arr[0]
            self.arr.pop()
            self.arr.pop(0)
            self.arr.insert(0,temp)
            QueueHeap.__downheap(self,0)

            return deq



    def size(self):
        return len(self.arr)



    def __upheap(self,r):
        parent = math.floor((r - 1) / 2)
        if (r!=0 and self.arr[parent] > self.arr[r]):
            t = self.arr[parent]
            self.arr[parent] = self.arr[r]
            self.arr[r] = t
            QueueHeap.__upheap(self,parent)


    def __downheap(self,r):

        lc = 2*r+1
        rc = lc+1
        min = lc
        if(lc > len(self.arr)-1):
            return None
        if(rc > len(self.arr)-1):
            return None

        if(self.arr[lc]>self.arr[rc]):
            min = rc
        else:
            min = lc

        if(self.arr[r]>self.arr[min]):
            temp = self.arr[r]
            self.arr[r] = self.arr[min]
            self.arr[min] = temp
            QueueHeap.__downheap(self,min)






