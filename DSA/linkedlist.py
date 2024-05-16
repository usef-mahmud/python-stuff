class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class List():
    def __init__(self, head: Node) -> None:
        self.head: Node = head

    def add_first(self, node: Node) -> None:
        node.next = self.head
        self.head = node
    
    def add_last(self, node: Node) -> None:
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    def out(self) -> None:
        curr = self.head
        print(curr.data)
        while curr.next != None:
            curr = curr.next
            print(curr.data)
    
    def length(self) -> int:
        l = 1
        curr = self.head
        while curr.next != None:
            l += 1
            curr = curr.next
        return l

    def get_node(self, idx: int) -> Node:
        if idx == 0:
            return self.head
        else:
            curr = self.head
            while idx and curr.next != None:
                curr = curr.next
                idx -= 1
            return curr

first = Node('first')
second = Node('second')
third = Node('third')

test = List(first)
test.add_last(second)
test.add_last(third)

test.out()
print(test.get_node())

import bs4