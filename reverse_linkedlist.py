class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


if __name__ == "__main__":
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)
    rll = reverse_linked_list(ll)
    while rll:
        print(rll.data)
        rll = rll.next
