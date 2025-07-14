"""
원형 큐 (Circular Queue)
 선형 큐의 메모리 낭비 문제(앞쪽 공간이 비어도 재사용 불가)를 해결하기 위한 자료구조
 고정 크기의 배열 기반으로, 포인터가 순환하도록 설계되어 공간을 효율적으로 사용
 크기 고정 → 큐가 다 찼을 때 사용 목적에 따라 overwrite를 허용하기도 한다.
    (이 파일에 overwrite 사용 유무로 클래스 2개 구현)
 시간 복잡도: enqueue, dequeue 모두 O(1), 단순한 포인터 연산

활용 예시
 1. 운영체제 - Round Robin CPU 스케줄링 (프로세스들 사이에 우선순위를 두지 않고 순서대로 CPU를 할당)
 2. 네트워크 - 패킷 수신 버퍼, 인터럽트 큐 (고정 크기에서 overflow 방지)
 3. 데이터 스트림 - 오디오/비디오 플레이어 버퍼 관리 (새로운 데이터가 들어오면 가장 오래된 데이터를 덮어씀)
"""

class BoundedCircularQueue:
    """ 큐가 다 차면 enqueue 실패(overwrite 허용 x), 더미칸 방식 이용 """

    def __init__(self, k: int):
        self.queue = [None] * (k + 1)
        self.max_size = k + 1
        self.front = 0
        self.rear = 0

    def enqueue(self, value) -> bool:
        if self.is_full():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        return True

    def dequeue(self) :
        if self.is_empty():
            return None
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        return val

    def get_front(self) :
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_rear(self) :
        if self.is_empty():
            return None
        return self.queue[(self.rear - 1 + self.max_size) % self.max_size]

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return (self.rear + 1) % self.max_size == self.front

    def size(self) -> int:
        return (self.max_size + self.rear - self.front) % self.max_size



class OverwriteCircularQueue:
    """ 덮어쓰기 방식 (overwrite 허용)
    큐가 다 차면 가장 오래된 항목 덮어씀 """

    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_size = k
        self.count = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, value) :
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        if self.is_full():
            self.front = (self.front + 1) % self.max_size
        else :
            self.count += 1

    def dequeue(self) :
        if self.is_empty() :
            return None
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return val

    def get_front(self) :
        return self.queue[self.front]

    def get_rear(self) :
        return self.queue[(self.max_size+self.rear-1)%self.max_size]

    def is_empty(self):
        return self.count == 0

    def is_full(self) :
        return self.max_size == self.count

    def size(self):
        return self.count



def test_bounded():
    print("=== BoundedCircularQueue Test ===")
    cq = BoundedCircularQueue(3)
    print(f"enqueue : {cq.enqueue(1)} {cq.enqueue(2)} {cq.enqueue(3)} {cq.enqueue(4)} (4번째 인큐 실패)")
    print(f"dequeue : {cq.dequeue()}, front : {cq.get_front()}, rear : {cq.get_rear()}")
    print(f"size : {cq.size()}, is_empty : {cq.is_empty()}")

def test_overwrite():
    print("\n=== OverwriteCircularQueue Test ===")
    buffer = OverwriteCircularQueue(3)
    buffer.enqueue('A')
    buffer.enqueue('B')
    buffer.enqueue('C')
    print(buffer.queue, "front:", buffer.get_front(), " rear:", buffer.get_rear())  # ['A', 'B', 'C'], A, C
    buffer.enqueue('D')  # 덮어쓰기 발생: A 자리에 D 들어옴
    print("after overwrite :", buffer.queue, "front:",buffer.get_front(), " rear:",buffer.get_rear())  # ['D', 'B', 'C'], B, D
    print("dequeue", buffer.dequeue())  # B
    print("after dequeue :", buffer.queue, "front:",buffer.get_front(), " rear:",buffer.get_rear())  # ['D', None, 'C'], C, D

if __name__ == "__main__":
    test_bounded()
    test_overwrite()
