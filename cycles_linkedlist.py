class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def cycledetect(head):
    slow=head
    fast=head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        #if slow == fast:
            #return "cycle detected"
    #return "cycle not detected"

if __name__ == "__main__":
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    print(cycledetect(ll))
    ll.next.next.next = ll.next
    print(cycledetect(ll))


    