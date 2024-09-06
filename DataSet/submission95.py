class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

def main():
    dllist = DoublyLinkedList()
    dllist.insert_at_end(1)
    dllist.insert_at_end(2)
    dllist.insert_at_end(3)
    dllist.print_list()
    dllist.delete_node(2)
    dllist.print_list()

if __name__ == "__main__":
    main()
