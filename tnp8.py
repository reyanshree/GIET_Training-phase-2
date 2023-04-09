-'''class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list1=Linkedlist()
list1.headval=Node("mon")
e2=Node("tue")
e3=Node("wed")
list1.headval.nextval=e2
e2.nextval=e3
list1.listprint()'''
'''#adding a node at the begining
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def begining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode

list1=Linkedlist()
list1.headval=Node("mon")
e2=Node("tue")
e3=Node("wed")
list1.headval.nextval=e2
e2.nextval=e3
list1.begining("sun")
list1.listprint()'''
#adding a node at the end
'''class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def end(self,newdata):
        newnode=Node(newdata)
        if self.headval is None:
            self.headval=newnode
            return
        last=self.headval
        while(last.nextval):
            last=last.nextval
        last.nextval=newnode
list1=Linkedlist()
list1.headval=Node("mon")
e2=Node("tue")
e3=Node("wed")
list1.headval.nextval=e2
e2.nextval=e3
list1.end("fri")
list1.listprint()'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def between(self,midnode,newdata):
        if midnode is None:
            print("node is absent")
            return
        newnode=Node(newdata)
        newnode.nextval=midnode.nextval
        midnode.nextval=newnode
    def delete_begining(self):
        if self.headval is None:
            print("node is absent")
            return
        self.headval=self.headval.nextval
    def delete_end(self):
        if self.headval is None:
            print("node is absent")
            return
        n=self.headval
        while n.nextval.nextval is not None:
            n=n.nextval
        n.nextval=None
    def delete_between(self,midnode): #deln by address
        if midnode is None:
            print("node is absent")
            return
        midnode.nextval=midnode.nextval.nextval
#deletion by value
    def delete_value(self,x):
        if self.headval is None:
            print("node is absent")
            return
        if self.headval.dataval==x:
           self.headval=self.headval.nextval
           return
        n=self.headval
        while n.nextval is not None:
            if n.nextval.dataval==x:
                break
            n=n.nextval
        if n.nextval is None:
             print("item not found")
        else:
            n.nextval=n.nextval.nextval
#searchig an item
    def search(self,x):#
        if self.headval is None:
            print("node is absent")
            return
        n=self.headval
        while n is not None:
            if n.dataval==x:
                print("iem found")
                return True
            n=n.nextval
        print("item not found")
        return False
#count the no of nodes
    def get_count(self):
        if self.headval is None:
            return 0
        n=self.headval
        count=0
        while n is not None:
            count+=1
            n=n.nextval
        return count
    def insert_index(self,index,data):
        if index==1:
            newnode=Node(data)
            newnode.nextval=self.headval
            self.headval=newnode
        i=1
        n=self.headval
list1=Linkedlist()
list1.headval=Node("mon")
e2=Node("tue")
e3=Node("wed")
e4=Node("thu")
list1.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
list1.between(list1.headval.nextval,"fri")
list1.between(list1.headval.nextval.nextval,"sat")
list1.delete_begining()
list1.delete_end()
list1.delete_between(list1.headval)
list1.delete_value("sat")
list1.search("sat")
list1.search("wed")
list1.listprint()
print(list1.get_count())
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
    def joining(self):
        str1=""
        start=self.headval
        while(start is not None):
            if(start.dataval =='*' or start.dataval == '/'):
                if(start.nextval.dataval=='*' or start.nextval.dataval=='/'):
                    str1+=" "
                    str1+=(start.nextval.nextval.dataval).upper()
                    start=start.nextval.nextval.nextval
                else:
                    str1+=" "
                    start=start.nextval
            else:
                str1+=start.dataval
                start=start.nextval
        return str1
list1=Slinkedlist()
list1.headval=Node('A')
e1=Node('n')
e3=Node('*')
e4=Node('/')
e5=Node('a')
e6=Node('p')
e7=Node('p')
e8=Node('l')
e9=Node('e')
e10=Node('*')
e11=Node('a')
e12=Node('/')
e13=Node('d')
e14=Node('a')
e15=Node('y')
e16=Node('*')
e17=Node('*')
e18=Node('k')
e19=Node('e')
e20=Node('e')
e21=Node('p')
e22=Node('s')
e23=Node('/')
e24=Node('*')
e25=Node('a')
e26=Node('/')
e27=Node('/')
e28=Node('d')
e29=Node('o')
e30=Node('c')
e31=Node('t')
e32=Node('o')
e33=Node('r')
e34=Node('*')
e35=Node('a')
e36=Node('w')
e37=Node('a')
e38=Node('y')
#linking the list
list1.headval.nextval=e1
e1.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=e9
e9.nextval=e10
e10.nextval=e11
e11.nextval=e12
e12.nextval=e13
e13.nextval=e14
e14.nextval=e15
e15.nextval=e16
e16.nextval=e17
e17.nextval=e18
e18.nextval=e19
e19.nextval=e20
e20.nextval=e21
e21.nextval=e22
e22.nextval=e23
e23.nextval=e24
e24.nextval=e25
e25.nextval=e26
e26.nextval=e27
e27.nextval=e28
e28.nextval=e29
e29.nextval=e30
e30.nextval=e31
e31.nextval=e32
e32.nextval=e33
e33.nextval=e34
e34.nextval=e35
e35.nextval=e36
e36.nextval=e37
e37.nextval=e38
print(list1.joining())
        
