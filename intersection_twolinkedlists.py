class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def twolinkedlist_intersection(head1,head2):
    current1 = head1
    current2 = head2
    while (current1 != current2):
        current1 = current1.next if current1 else head1
        current2 = current2.next if current2 else head2
    if current1:
        return current1
    else:
        return None

if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    
    head2 = Node(6)
    head2.next = Node(7)
    #head2.next.next = head1.next.next
    
    intersection = twolinkedlist_intersection(head1,head2)
    
    if intersection:
        print(intersection.data)
    else:
        print("no intersection found")





