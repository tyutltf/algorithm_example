class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def push(self, d):
        self.data.append(d)

    def gettop(self):
        if self.isempty():
            return 'stack is empty'
        return self.data[-1]

    def pop(self):
        if self.isempty():
            return 'stack is empty'
        return self.data.pop()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('压入三个元素后:', stack.data)
print('此时栈顶元素为:', stack.gettop())
stack.pop()
print('一次出栈后:', stack.data)
