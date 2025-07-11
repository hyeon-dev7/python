import stack as s

"""
stack 이용 min 값 찾기
  입력 : 정수
  조건 및 결과
  1) 스택 2개 사용 가능
  2) push 된 값 중 min 값을 O(1) 시간에 구하기
  3) 데이터 pop()시 최소값이 제거 될 가능성 고려
  e.g. lst = [10,3,4,7,3,1,5] 입력 후 2회 pop -> 결과값 3
"""
class MinStack :
    def __init__(self):
        self.stack = s.Stack()
        self.min_stack = s.Stack()

    def push(self, val) :
        self.stack.push(val)
        if self.min_stack.is_empty() :
            self.min_stack.push(val)
        elif self.min_stack.peek() >= val :
                self.min_stack.push(val)


    def pop(self) :
        x = self.stack.pop()
        if self.min_stack.peek() == x :
            self.min_stack.pop()

    def get_min(self) :
        return self.min_stack.peek()



"""
stack 2개로 queue (enqueue, dequeue) 구현

평균 시간 복잡도 (Amortized)  O(1)
최악 시간 복잡도 (Worst case) O(n) - 디큐시 stack2가 비었을 때 stack1에서 모두 옮김
"""
class Queue:
    def __init__(self):
        self.stack1 = s.Stack() # in
        self.stack2 = s.Stack() # out

    def enqueue(self, val) :
        self.stack1.push(val)

    def dequeue(self):
        if self.is_empty() :
            return None
        if self.stack2.is_empty() :
            self._move()
        return self.stack2.pop()

    def peek(self): # 큐의 맨 앞 값을 제거하지 않고 반환
        if self.is_empty() :
            return None
        if self.stack2.is_empty() :
            self._move()
        return self.stack2.peek()

    def _move(self):
        while not self.stack1.is_empty() :
            self.stack2.push(self.stack1.pop())

    def clear(self):
        self.stack1.clear()
        self.stack2.clear()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self):
        return len(self.stack1) + len(self.stack2)
        # stack class에 __len__이 있어서 사용 가능




def test_minstack():
    print("=== MinStack Test ===")
    lst = [10, 3, 4, 7, 3, 1, 5]
    stack1 = MinStack()
    for x in lst:
        stack1.push(x)
    print("push", lst, "→ min : {}".format(stack1.get_min()))
    stack1.pop()
    stack1.pop()
    print("Minimum after pop twice :", stack1.get_min())  # 3


# 출력 기반 테스트기 직관적이지 않아 assert를 활용한 자동 검증 방식을 시도
def test_queue():
    print("\n=== Queue Test ===")
    queue = Queue()

    for i in range(5):
        queue.enqueue(i)
    assert queue.size() == 5
    assert queue.peek() == 0

    for _ in range(4):
        queue.dequeue()
    assert queue.peek() == 4
    assert queue.size() == 1

    for i in range(10, 15):
        queue.enqueue(i)
    assert queue.size() == 6

    assert queue.dequeue() == 4
    assert queue.dequeue() == 10

    queue.clear()
    assert queue.is_empty()
    assert queue.peek() is None

    print("All Queue tests passed.")

if __name__ == "__main__":
    test_minstack()
    test_queue()