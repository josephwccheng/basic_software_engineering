'''
Reference: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm#:~:text=A%20linked%20list%20is%20a,lists%20in%20its%20standard%20library.&text=In%20this%20type%20of%20data,between%20any%20two%20data%20elements.
'''

'''
A linked list is a sequence of data elements, which are connected together via links. 
Each data element contains a connection to another data element in form of a pointer. 
Python does not have linked lists in its standard library.
We implement the concept of linked lists using the concept of nodes
'''


'''
singly linked lists
In this type of data structure there is only one link between any two data elements. 
We create such a list and create additional methods to insert, update and remove elements from the list.
'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def print(self):
        cur = self.headval
        while cur is not None:
            print (cur.val)
            cur = cur.next
    def InsertAtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.next = self.headval
        self.headval = NewNode

# Creating our linked list with three nodes

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.next = e2
# Link second Node to third node
e2.next = e3

''' Traversing a Linked Lists 
by looping through the list and printing out all values 
Singly linked lists can be traversed in only forwrad direction starting form the first data element. 
We simply print the value of the next data element by assgining the pointer of the next node to the current data element.
'''
print("First Transfersing of Linked List")
list1.print()

''' Insertion in a Linked List 
Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted node.
'''
print("Inserted Sunday to the Linked List at the beginning")
list1.InsertAtBegining("Sun")
list1.print()


