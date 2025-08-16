"""
양방향 연결 리스트
 각 노드가 앞/뒤 노드를 가리키는 두 개의 포인터(prev, next)와 데이터를 가지고 있는 자료 구조
 양방향 탐색(순방향 및 역방향) 가능
 단방향 연결 리스트에 비해 포인터 1개가 추가되어 메모리 사용량 증가

연산 시간 복잡도
 - push_front / pop_front : O(1)
 - push_back / pop_back : O(1)
 - insert / delete (노드를 알고 있는 경우) : O(1)
 - search : O(N)

공간 복잡도 : O(N)
 - 전체 노드 수(N)에 비례

※ 더미 헤드와 더미 테일을 사용하여 예외 처리를 단순화했습니다.
"""

class Node:
    def __init__(self, key=None, owner=None):
        self.key = key
        self.next = self
        self.prev = self
        self.owner = owner

    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(owner=self)
        self.tail = Node(owner=self)
        self.head.next = self.tail
        self.tail.prev = self.head


    def splice(self, start_node, end_node, insert_after):
        """start_node부터 end_node까지의 구간을 잘라내어 insert_after 뒤에 삽입"""
        if (start_node in (start_node.owner.head, start_node.owner.tail)
                or end_node in (end_node.owner.head, end_node.owner.tail)
                or insert_after == self.tail):
            return  # 더미 노드 조작 방지
        if start_node is None or end_node is None or insert_after is None:
            return
        if start_node is end_node and insert_after.next is start_node:
            return # no-op : 이미 원하는 위치에 있어 실제 이동이 필요 없음
        if not self._is_valid_splice(start_node, end_node, insert_after):
            return

        # 잘라내기
        sp = start_node.prev
        en = end_node.next
        sp.next = en
        en.prev = sp
        # 삽입
        xn = insert_after.next
        insert_after.next = start_node
        start_node.prev = insert_after
        xn.prev = end_node
        end_node.next = xn

        # owner 업데이트 (다른 리스트에서 가져오는 경우에만)
        if start_node.owner != self :
            self.update_owner(start_node, end_node)


    def _is_valid_splice(self, start, end, after):
        """
        splice 연산 수행 전 조건 확인 :
        1) start와 end는 같은 리스트에 속해야 함
        2) start → end 구간이 연결되어 있어야 함
        3) after가 해당 구간 안에 있으면 안 됨
        4) after는 현재 리스트(self)에 속해 있어야 함
        """
        if start.owner != end.owner:
            return False

        curr = start
        found_end = False
        while curr and curr != start.owner.tail:
            if curr is after:
                return False
            if curr == end:
                found_end = True
                break
            curr = curr.next

        if not found_end:
            return False
        return after.owner == self


    def update_owner(self, start, end):
        curr = start
        while curr != end.next:
            curr.owner = self
            curr = curr.next


    def move_after(self, node, insert_after):
        """ node를 insert_after 뒤로 이동
        node와 insert_after가 해당 리스트에 속하지 않으면 아무 작업도 하지 않고 None 반환 """
        if node.owner != self or insert_after.owner != self :
            return None
        if node.prev is insert_after: # no-op
            return
        self.splice(node, node, insert_after)

    def move_before(self, node, insert_before):
        """ node를 insert_before 앞으로 이동
        node와 insert_before가 해당 리스트에 속하지 않으면 아무 작업도 하지 않고 None 반환"""
        if node.owner != self or insert_before.owner != self :
            return None
        if node.next is insert_before: # no-op
            return
        self.splice(node, node, insert_before.prev)


    def push_front(self, key):
        """리스트 맨 앞(head 다음)에 새 노드 추가"""
        node = Node(key, self)
        self.splice(node, node, self.head)

    def push_back(self, key):
        """리스트 맨 앞(head 다음)에 새 노드 추가"""
        node = Node(key, self)
        self.splice(node, node, self.tail.prev)

    def insert(self, node, key):
        """주어진 node 앞에 새 값을 삽입"""
        if node is None or node == self.head:
            return False
        curr = self.head.next
        while curr != self.tail :
            if curr == node:
                new = Node(key, self)
                self.splice(new, new, node.prev)
                return True
            curr = curr.next
        return False

    def pop_front(self):
        """가장 앞 노드(첫 데이터 노드)를 제거하고 key 반환"""
        if self.head.next == self.tail:
            return None
        key = self.head.next.key
        self._remove(self.head.next)
        return key

    def pop_back(self):
        """가장 뒤 노드(마지막 데이터 노드)를 제거하고 key 반환"""
        if self.head.next == self.tail:
            return None
        key = self.tail.prev.key
        self._remove(self.tail.prev)
        return key

    def delete(self, node):
        """ node를 찾아 제거 (존재할 때만 삭제)"""
        if node and node != self.head and node != self.tail:
            curr = self.head.next
            while curr != self.tail:
                if curr == node:
                    key = node.key
                    self._remove(node)
                    return key
                curr = curr.next
        return None

    def _remove(self, node):
        """내부 전용 제거 함수"""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None # 참조 해제
        node.owner = None
        del node

    def size(self):
        """내부 전용 제거 로직"""
        count = 0
        curr = self.head.next
        while curr != self.tail:
            count += 1
            curr = curr.next
        return count

    def is_empty(self):
        """리스트가 비어있는지 여부"""
        return self.head.next is self.tail

    def clear(self):
        """모든 노드 제거 (리스트 초기화)"""
        curr = self.head.next
        while curr != self.tail:
            nxt = curr.next
            self._remove(curr)
            curr = nxt
        self.head.next = self.tail
        self.tail.prev = self.head

    def search(self, key):
        """key 값을 가진 노드 탐색"""
        curr = self.head.next
        while curr != self.tail:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def __iter__(self):
        """이터레이터 (리스트 순회용)"""
        node = self.head.next
        while node != self.tail:
            yield node.key
            node=node.next

    def __str__(self):
        """문자열로 출력 """
        return ' ⇆ '.join(map(str, self.__iter__()))

    def reverse1(self):
        """리스트 전체를 역순으로 뒤집음"""
        if self.head.next == self.tail:
            return self

        curr = self.head.next
        prv = None
        while curr != self.tail:
            nxt = curr.next
            curr.next = prv
            curr.prev = nxt
            prv = curr
            curr = curr.prev

        new_first = self.tail.prev
        new_last = self.head.next

        self.head.next = new_first
        new_first.prev = self.head

        self.tail.prev = new_last
        new_last.next = self.tail
        return self
