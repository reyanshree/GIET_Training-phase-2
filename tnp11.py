'''def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):#left-root-right
    if root:
        inorder(root.left)
        print(str(root.key)+"->",end="")
        inorder(root.right)
def preorder(root): #root-left-right
    if root:
        print(str(root.key)+"->",end="")
        preorder(root.left)
        preorder(root.right)
def postorder(root):#left-right-root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key)+"->",end="")
def insert(node,key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def min_val_node(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def del_node(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=del_node(root.left,key)
    elif(key>root.key):
        root.right=del_node(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=min_val_node(root.right)
        root.key=temp.key
        root.right=del_node(root.right,temp.key)
    return root'''
'''def del_node(root,key):
    
#root=node(1)
#root.left=node(2)
#root.right=node(3)
#root.left.left=node(4)
#root.left.right=node(5)
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("inorder traversal")
inorder(root)
root=del_node(root,8)
print("\ninorder traversal after deleting 8")
inorder(root)
root=del_node(root,4)
print("\ninorder traversal after deleting 4")
inorder(root)'''
'''print("\npreorder traversal")
preorder(root)
print("\npostorder traversal")
postorder(root)'''
#even odd queue
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
queue1=Queue(7)
print("is it full",queue1.is_full())
print("is it empty",queue1.is_empty())
queue1.enqueue(2)
queue1.display()
queue1.enqueue(7)
queue1.display()
queue1.enqueue(9)
queue1.display()
queue1.enqueue(4)
queue1.display()
queue1.enqueue(6)
queue1.display()
queue1.enqueue(5)
queue1.display()
queue1.enqueue(10)
queue1.display()
print("elements deleted",queue1.dequeue())
queue.display()
#merging the list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
   
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while(temp):

            print(temp.data, end=" ")
            temp=temp.next
    def merge(self, newElement, position):
        newNode = Node(newElement)
        if (position == 1):
            newNode.next = self.head
            self.head = newNode
        else:    
            temp = self.head
            for i in range(1, position):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode  
            else:
                print("\nThe previous node is null.")                        
list1=Linkedlist()
list1.push(1)
list1.push(2)
list1.push(4)
list1.push(3)
list1.push(5)
print("linked list1 is")
list1.printlist()
list2=Linkedlist()
list2.push(9)
list2.push(8)
list2.push(11)
print("\nlinked list2 is")
list2.printlist()
list3=Linkedlist()
list3.merge(1)
print("\nlinked list3 is")
#replacing maximum element by a given element
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
   
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next
    def largest(head):
        max=-32767
        while(head is not None):
            if(max<head.data):
                max=head.data
            head=head.next
        return max
list1=Linkedlist()
list1.push(1)
list1.push(2)
list1.push(4)
list1.push(3)
list1.push(5)
print("linked list1 is")
list1.printlist()

