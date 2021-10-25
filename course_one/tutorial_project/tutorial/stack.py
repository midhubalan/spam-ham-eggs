"""class demo using stack"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    
    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x} of size {len(self)}>'

def main():
    a_stack = Stack()
    a_stack.push('hello')
    a_stack.push('world')
    print(a_stack)
    print(a_stack.pop())
    print(len(a_stack))

if __name__ == '__main__':
    main()