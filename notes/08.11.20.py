class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = newNode
        return self

    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)

    def addFront(self, val):
        # create new node
        newNode = Node(val)

        # give new node current self.head
        newNode.next = self.head

        #  replace self.head new node
        self.head = newNode

        # chaining
        return self

    def removeFront(self):
        self.head = self.head.next


newSLL = SLL()
newSLL.append(5).append(8).addFront(28).append(12).display()
