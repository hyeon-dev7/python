class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self)==0:
            return None
        return self.items.pop()
        # try :
        #     return self.items.pop()
        # except IndexError :
        #     print("Stack is empty")
        #     return None

    def peek(self):
        if len(self) == 0:
            return None
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0
        # len()을 만나면 class 내부에서 __len__을 찾음

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s) # __str__
    print("Top :", s.peek())
    print("Pop :", s.pop())
    print("Stack length :", len(s))
    s.clear()
    print("Is empty :", s.is_empty())
