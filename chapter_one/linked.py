class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class singlelikn:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return

    def isempty(self):
        return self.length == 0
