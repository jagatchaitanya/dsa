class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def position_insert(self,position,value):
        new_node=Node(value)
        counter = 0
        current_node = self.head
        while current_node.next and counter<position-1:
            current_node = current_node.next
            counter = counter + 1
        temp = current_node.next
        current_node.next = new_node
        current_node.next.next = temp
    def print_list(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data,end="->")
            current_node = current_node.next
        print(current_node.data)


