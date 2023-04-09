'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current =self.head
        while(current is not None):# is not None can be ignored
              next=current.next
              current.next=prev
              prev=current
              current=next
        self.head=prev
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next
list1=Linkedlist()
list1.push(20)
list1.push(5)
list1.push(15)
list1.push(35)
print("linked list is")
list1.printlist()
list1.reverse()
print("\nreverse linked list is")           
list1.printlist() '''

'''class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    def insert_start(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    def insertAtEnd(self,value):
        new_node= Node(value)
        if self.isEmpty():
             self.insert_start(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp = temp.next
    def delete_start(self):
         if self.isEmpty():
            print("linked list is empty.cannot delete elements")
         elif self.head.next is None:
             self.head=None
         else:
             self.head=self.head.next
             self.head.prev=None               
    def delete_last(self):
        if self.isEmpty():
            print("linked list is empty.cannot delete elements")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None
    def del_posn(self,posn):
        if self.isEmpty:
            print("linked list is empty.cannot delete elements")
        elif posn==1:
            self.delete_start()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==posn:
                    break
                temp=temp.next
                count+=1
            if temp is None:
               print("there is no element to print")
            elif temp.next is None:
                self.delete_last()
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
            
            
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
#x.delete_start()
x.delete_last()
x.printLinkedList()
x.del_posn(2)
x.printLinkedList()'''
#postfix evaluation
class evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isempty():
            self.top-=1
            return self.array.pop()
        else:
            return"$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def evl_postfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2 + i+ val1)))
        return int(self.pop())

exp="231*+9-"
obj=evaluate(len(exp))
print(obj.evl_postfix(exp))
class Node:
    def __init__(self,value):
        self.previous= None
        self.data = value
        self.next = None
class DoublyLinkedList:
        def __init__(self):
            self.head = None
        def isEmpty(self):
            if self.head is None:
                return True
            return False
        def length(self):
            temp = self.head
            count = 0
            while temp is not None:
                temp = temp.next
                count +=1
            return count
        def insertAtBeginning(self,value):
            new_node = Node(value)
            if self.isEmpty():
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
        def insertAtEnd(self,value):
            new_node = Node(value)
            if self.isEmpty():
                self.insertAtBeginning(value)
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
        def insertAtPosition(self,value,position):
            temp = self.head
            count = 1 
            while temp is not None:
                if count == position - 1:
                    break
                count +=1 
                temp = temp.next
            if position == 1:
                self.insertAtBeginning(value)
            elif temp is None:
                print("There are less than {}-1 elements in the linked list".format(position,position))
            elif temp.next is None:
                self.insertAtEnd(value)
            else:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.previous = temp
                temp.next.previous = new_node
                temp.next= new_node
        def printLinkedList(self):
            temp = self.head
            while temp is not None:
                print(temp.data, sep=",")
                temp = temp.next
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
print("insert at position 2 number 8")
x.insertAtPosition(8,2)
x.printLinkedList()
#question 1
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Slinkedlist:
    def __init(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def insert_node(self,pos_insert,val_insert):
        pos=self.headval
        c=1
        while(pos is not None):
            if(c == pos_insert-1):
                break
            else:
                c+=1
                pos=pos.nextval
        newnode=Node(val_insert)
        newnode.nextval=pos.nextval
        pos.nextval=newnode
    def view_node(self,pos):
        pos_node=self.headval
        c=1
        while(pos is not None):
            if(c == pos):
                break
            else:
                c+=1
                pos_node=pos_node.nextval
        return (pos_node.dataval)
list1=Slinkedlist()
list1.headval=Node(89)
e1=Node(78)
e2=Node(99)
e3=Node(76)
e4=Node(77)
e5=Node(67)
e6=Node(99)
e7=Node(98)
e8=Node(90)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
list1.listprint()
n=int(input("Enter the value to be inserted"))
i=int(input("Enter the position"))
list1.insert_node(i,n)
print("After insertion")
list1.listprint()
print("mark of 5th person is",list1.view_node(5))
print("mark of 7th person is",list1.view_node(7))
#question 2
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
list3=[]
for i in list1:
    for j in list2:
        if i*2==j:
            list3.append(i)
print(list3)


    
