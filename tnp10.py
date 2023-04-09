#linear search
def ls(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=1
n=len(array)
result=ls(array,n,x)
if(result==-1):
    print("element not found")
else:
    print("element found at index:",result)
#binary search
def bs(array,x,low,high):
    while low<=high:
        mid=(high-low//2)
        if(array[mid]==x):
            return mid
        elif(x<array[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1
array=[3,4,5,6,7,8,9]
x=40
result=bs(array,x,0,len(array)-1)
if(result==-1):
    print("element not found")
else:
    print("element found at index:",result)

#binary tree traversal
class Node:
    def __init__(self,key):
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
root=insert(root,14)
root=insert(root,4)
print("inorder traversal")
inorder(root)
print("\npreorder traversal")
preorder(root)
print("\npostorder traversal")
postorder(root)
#question 1
'''A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node refers to a compartment.'''
class node:
     def __init__(self,data=None):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self,new_data):
        self.head=None
    def push(self):
        if self.head is None:
            new_node=node(new_data)
   # def insert(self,new_data):
       # new_node=node(new_data)
       # new_node.next=self.head
       # self.head=new_node    
    def search(self,x):
        if self.head is None:
            print("node is absent")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                print("iem found")
                return True
            n=n.next
        print("item not found")
        return False
    def print(self):
        val=self.head
        while val is not None:
            print(val.data)
            val=val.next
class train:
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.compartment_list=compartment_list   
class compartment:
    def __init__(self,compartment_name,total_seats,no_of_passenger):
        self.compartment_name=compartment_name
        self.total_seats=total_seats
        self.no_of_passenger=no_of_passenger
    def count_compartments(self):
        temp=self.compartment_list.head()
        count=0
        while(temp):
            count+=1
        temp=temp.next()
    def check_vacancy(self):
        temp=self.compartment_list.head()
        count=0
        while(temp):
            percentage=(temp.data.total_seats-temp-temp.data.no_of_passenger//temp.data.total_seat)
            if percentage>0.5:
                count+=1
                temp=temp.next()
            return count
comp1=compartment("s1",500,200)
comp2=compartment("s2",250,250)
comp3=compartment("s3",300,150)
comp4=compartment("s4",400,100)
comartment_list=Linkedlist()
compartment_list.push(comp1)
compartment_list.push(comp2)
compartment_list.push(comp3)
compartment_list.push(comp4)
train1=train("rajyarani",comartment_list)
count=train1. count_compartments
print(count)
vacancy=train1.check_vacancy
print(count1)
 
                                          


        
        
