class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top item:", stack.peek())
    print("Stack size:", stack.size())
    stack.pop()
    print("Stack after pop:", stack.stack)

if __name__ == "__main__":
    main()
