"""
단방향(한방향) 연결 리스트
 각 노드가 데이터와 다음 노드를 가리키는 포인터(next)를 가지고 있는 자료 구조
 이전 노드를 가리키는 포인터가 없기 때문에 이전 노드로 돌아갈 수 없고, 단방향 탐색만 가능

연산 시간 복잡도
 - push_front / pop_front : O(1)
 - push_back / pop_back : O(N), 마지막 노드를 찾기 위해 처음부터 탐색해야 함
 - search : O(N)

공간 복잡도 : O(N)
 노드 하나당 데이터 + 포인터 1개 공간 필요
 메모리 사용량이 전체 노드 수(N)에 비례
"""

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None # link

    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = Node() # 더미 헤드
        self.__size = 0

    def push_front(self, key):
        new_node = Node(key)
        new_node.next = self.head.next
        self.head.next = new_node
        self.__size += 1

    def push_back(self, key):
        new_node = Node(key)
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.next = None
        self.__size += 1


    def insert(self, idx, key):
    # linked list는 index로 접근할 수 없지만 가독성을 위해 idx라는 이름을 사용
        if idx ==0 :
            self.push_front(key)
        elif idx ==self.__size:
            self.push_back(key)

        elif 0< idx < self.__size:
            new_node = Node(key)
            prev = self.head
            for i in range(idx):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            self.__size += 1

        else:
            raise IndexError("범위를 벗어났습니다.")


    def pop_front(self):
        if self.__size == 0:
            return None
        return self._remove(self.head, self.head.next)

    def pop_back(self):
        if self.__size == 0 :
            return None
        else :
            prev = self.head
            tail = prev.next
            while tail.next is not None:
                prev = tail
                tail = tail.next
            return self._remove(prev, tail)

    def delete(self, idx):
        if 0<= idx < self.__size:
            prev = self.head
            target = prev.next
            for i in range(idx):
                prev = target
                target = prev.next
            return self._remove(prev, target)
        else:
            return None

    def delete_node(self, node):
        prev, target = self.head, self.head.next
        while target :
            if target == node :
                return self._remove(prev, target)
            prev, target = target, target.next
        return None

    def _remove(self, prev, target):
        """prev와 target 노드 기반 삭제 (공통 내부 메서드)"""
        prev.next = target.next
        key = target.key
        self.__size -= 1
        del target
        return key


    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.head.next = None
        self.__size = 0

    def search(self, key):
        for node in self:
            if node.key == key:
                return node
        return None

    def search_idx(self,key):
        for i, node in enumerate(self):
            if node.key == key :
                return i
        return -1

    def __iter__(self) : # generator
        node = self.head.next
        while node:
            yield node
            node = node.next

    def __str__(self):
        return ' → '.join(str(node) for node in self)

    def reverse1(self): # 연결 순서 뒤집기, 파괴적 함수
        prev = None
        curr = self.head.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head.next = prev
        return self
