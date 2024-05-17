class Node():
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.next: Node = None

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
    
    def add(self, idx: int, node: Node) -> None:
        if idx < self.length() - 1:
            curr = self.head
            while idx and curr.next != None:
                curr = curr.next
                idx -= 1
            node.next = curr.next
            curr.next = node
            
        else:
            print('out of scope')

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
        """
        This method gets the index of node you're searcing for and return it.

        If index exceeds the length of list, it will return the last node. 
        """
        if idx == 0:
            return self.head
        else:
            curr = self.head
            while idx and curr.next != None:
                curr = curr.next
                idx -= 1
            return curr
    
    def pop_start(self) -> None:
        poped = self.head
        self.head = poped.next

    def pop_end(self) -> None:
        curr = self.head
        while curr.next.next != None:
            curr = curr.next

        curr.next = None

    def del_node(self, idx: int) -> str:
        if idx < self.length() - 1:
            deleted = Node()
            # code goes here
            return deleted.data
        else:
            print('out of scope')

nodes = []
for i in range(1, 11):
    nodes.append(Node(f'node #{i}'))

linked = List(Node('first'))
for node in nodes:
    linked.add_last(node)

linked.pop_start()
linked.pop_start()
linked.pop_end()
linked.pop_end()
linked.pop_end()
linked.pop_end()

linked.out()
print(f'now length is: {linked.length()}')

'''
[DONE] delete from beginning and end
[ ] delete from
[DONE] insert at middle

'''