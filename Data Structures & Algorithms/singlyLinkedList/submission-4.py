class LinkedList:
    class Node:
        val = None
        next = None
        def __init__(self, val):
            self.val = val

    head = None
    tail = None
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range (0, index):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
                return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        node = self.Node(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        node = self.Node(val)
        if self.tail != None:
            self.tail.next = node
        if self.head is None:
            self.head = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prev = None
        curr = self.head
        j = 0
        while j != index and curr != None:
            prev = curr
            curr = curr.next
            j += 1
        if curr is None:
            return False
        # Head case
        if prev is None:
            self.head = curr.next
        # Tail case
        elif curr.next is None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return vals