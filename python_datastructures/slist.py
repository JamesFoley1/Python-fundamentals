class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node

    def removeNode(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return True
        else:
            current = self.head.next
            previous = self.head
            while current:
                if current.value == value:
                    previous.next = current.next
                    return True
                else:
                    previous = current
                    current = current.next
            return False
        
    def insertNode(self, value, index):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
    
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
    
list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.insertNode(4, 1)
list.printAllValues("Test Remove")