class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sortedlinkedlist(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next

if __name__=="__main__":
    ll1 = Node(1)
    ll1.next = Node(3)
    ll1.next.next = Node(5)
    ll1.next.next.next = Node(7)
    
    ll2 = Node(2)
    ll2.next = Node(4)
    ll2.next.next = Node(6)

    # Merging the lists
    merged_head = merge_sortedlinkedlist(ll1, ll2)

    # Print the merged list
    current = merged_head
    while current:
        print(current.data, end=" ")
        current = current.next




