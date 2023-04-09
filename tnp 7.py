class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.elements=[None]*self.__max_size
        self.__top=-1
    def is__full(self):
        if(self.__top==self.max_size-1):
            return True
        return False
    def is__empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("the stack is empty")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if (self.is_empty()):
            print("the stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self._-max_size
ball_stack=stack(4)
print("is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display(6)
print("size of the stack",ball_stack.get_max_size())
print("the element deleted",ball_stack.pop())
print("after deleting the element")
ball_stack.display()
print("size of the stack",ball_stack.get_maxsize())


class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.max_size
        self.__rear=-1
        self.front=0
    def is_full(self):
        if(self.rear==self.__max_size-1):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is__empty()):
            print("Queue is empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
        def display(self):
            for index in range (self.__front,self.__rear):
                print(self.elements[index])
        def get_max_size(self):
            return self.__max_size
queue1=Queue(4)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("elements deleted",queue1.dequeue())
queue.display()#question-1
class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=0
        self.rear=-1
    def isempty(self):
        if(self.front>self.rear):
            return True
        return False
    def isfull(self):
        if(self.rear==self.maxsize-1):
            return True
        return False
    def enqueue(self,data):
        if(self.isfull()):
            print("queue is full",data,"cannot be added to queue")
        else:
            self.rear+=1
            self.queue[self.rear]=data
            print(data)
    def dequeue(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            val = self.queue[self.front]
            self.front+=1
            print(val,"is dequeued")
    def display(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
    def max_size(self):
        return self.maxsize

q1=queue(5)
q1.enqueue(13983)
q1.enqueue(10080)
q1.enqueue(7113)
q1.enqueue(2520)
q1.enqueue(2500)

start=q1.front
end=q1.rear

print("even nos are")
for i in range(start,end+1):
    res=1
    for j in range(1,11):
        if(q1.queue[i]%j!=0):
            res=0
            break
    if(res==1):
        print(q1.queue[i])

#question 2
l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
for i in range(len(l1)):
    if l1[i]!=None and l2[-(i+1)]!=None:
        print( l1[i]+l2[-(i+1)],end=' ')
    elif l1[i]==None:
        print(l2[-(i+1)],end=' ')
    else:
        print( l1[i],end=' ')


        

