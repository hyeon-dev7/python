"""
MinHeap (배열 기반 최소 힙)
 - 최소값을 빠르게 조회 및 제거할 수 있는 힙 자료구조
 - heapify-up / heapify-down을 통해 힙 조건(부모<=자식) 유지
 - 완전 이진 트리를 배열로 표현(포인터 없이 부모-자식 관계 설정) → 공간을 효율적으로 사용
 - 우선순위 큐로 활용 가능

🕒 시간 복잡도
 - push(value): O(log n)                 # 값 삽입 후 heapify-up
 - pop(): O(log n)                       # 루트 제거 후 heapify-down
 - peek(): O(1)                          # 루트 값 조회
 - replace_root(value): O(log n)         # 루트 교체 후 heapify-down
 - try_pushpop(value): O(log n) 또는 O(1) # 조건에 따라 삽입 또는 제거
 - build_heap(iterable): O(n)            # 초기 힙 구성 (bottom-up 방식)
 - heap_sort(): O(n log n)               # 힙을 이용한 정렬
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """ 값 삽입 후 정렬 (heapify-up) """
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def pop(self):
        """ 최소값 제거 및 반환 (heapify-down) """
        if not self.heap :
            return None
        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        val = self.heap.pop()
        self._heapify_down(0, last_index)
        return val

    def peek(self):
        """ 최소값 조회 """
        if self.size() == 0:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        """ 부모와 비교하며 최소 힙 조건을 만족하도록 위로 이동 """
        while index > 0 :
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index] :
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else :
                break

    def _heapify_down(self, index, size):
        """ 루트 값을 자식과 비교하여 최소 힙 조건을 만족하도록 아래로 이동 """
        while 2 * index +1 < size :
            l, r = 2 * index +1, 2 * index + 2
            if self.heap[l] < self.heap[index] :
                min_idx = l
            else:
                min_idx = index
            if r < size and self.heap[r] < self.heap[min_idx] :
                min_idx = r
            if min_idx != index :
                self.heap[index], self.heap[min_idx] = self.heap[min_idx], self.heap[index]
                index = min_idx
            else:
                break


    def size(self):
        """ 힙에 저장된 요소의 개수를 반환 """
        return len(self.heap)

    def clear(self):
        """ 힙 초기화 """
        self.heap = []

    def is_empty(self):
        """ 힙이 비어있는지 확인 """
        return self.size() == 0

    @classmethod
    def build_heap(cls, iterable):
        """ 반복 가능한 객체로부터 힙 생성 """
        heap = cls()
        heap.heap = list(iterable)
        n = len(iterable)
        for i in range(n//2, -1, -1) :
            heap._heapify_down(i, n)
        return heap

    def replace_root(self, value):
        """ 최소값 제거 후 새 값 삽입 (heapq.heapreplace) """
        n = len(self.heap)
        if n==0 :
            return None
        key = self.heap[0]
        self.heap[0] = value
        self._heapify_down(0, n)
        return key


    def try_pushpop(self, value):
        """ 조건부 삽입 후 최소값 제거 (heapq.heappushpop)
        - value < heap[0]이면 삽입되지 않고 value 반환
        - value ≥ heap[0]이면 heap[0] 제거 후 value 삽입
         """
        if self.is_empty() : return None
        if value < self.heap[0] :
            return value
        else:
            return self.replace_root(value)

    def heap_sort(self):
        """ 오름차순으로 정렬된 결과 반환, 원본은 유지 """
        copy = self.heap[:]
        for i in range(len(copy)-1, 0, -1) :
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self._heapify_down(0, i)
        self.heap, copy = copy, self.heap
        return copy[::-1]


    def to_list(self):
        """ 힙의 내부 배열을 복사하여 반환 """
        return self.heap[:]
