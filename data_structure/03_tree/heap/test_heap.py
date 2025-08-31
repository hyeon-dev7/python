import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_push_and_pop(self):
        self.heap.push(5)
        self.heap.push(3)
        self.heap.push(7)
        self.heap.push(1)
        self.heap.push(3)
        self.assertEqual(self.heap.to_list(), [1, 3, 7, 5, 3])
        pop_lst = []
        while not self.heap.is_empty() :
            pop_lst.append(self.heap.pop())
        self.assertEqual(pop_lst, [1, 3, 3, 5, 7])

        for v in [7, -7, 9, -4]:
            self.heap.push(v)
        self.assertEqual(self.heap.pop(), -7)
        self.assertEqual(self.heap.pop(), -4)
        self.assertFalse(self.heap.is_empty())
        self.assertEqual(self.heap.pop(), 7)
        self.assertEqual(self.heap.pop(), 9)
        self.assertTrue(self.heap.is_empty())


    def test_peek(self):
        self.assertIsNone(self.heap.peek())
        self.heap.push(10)
        self.assertEqual(self.heap.peek(), 10)
        self.heap.push(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.push(7)
        self.assertEqual(self.heap.peek(), 5)


    def test_size_empty(self):
        self.assertEqual(self.heap.size(), 0)
        self.assertTrue(self.heap.is_empty())
        self.heap.push(1)
        self.assertEqual(self.heap.size(), 1)
        self.heap.push(2)
        self.assertEqual(self.heap.size(), 2)
        self.assertFalse(self.heap.is_empty())


    def test_multiple_heapify_down(self):
        # 이 입력은 pop 후 루트가 9가 되고, 3 → 2 → 1 순으로 내려가야 함
        for val in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.heap.push(val)

        # 내부 구조 확인 (루트가 최소값)
        self.assertEqual(self.heap.to_list()[0], 1)

        # pop() → 1 제거, 9이 루트로 올라옴 → 여러 번 heapify_down 발생
        popped = self.heap.pop()
        self.assertEqual(popped, 1)

        # 루트가 다시 최소값이 되었는지 확인
        self.assertEqual(self.heap.to_list()[0], 2)

        # 전체 pop 결과 확인
        result = []
        while not self.heap.is_empty():
            result.append(self.heap.pop())
        self.assertEqual(result, [2, 3, 4, 5, 6, 7, 8, 9])


    def test_heap_sort(self):
        for val in [5, 3, 7, 1, 4]:
            self.heap.push(val)
        self.assertEqual(self.heap.heap_sort(), [1, 3, 4, 5, 7])
        self.assertEqual(self.heap.to_list(), [1, 3, 7, 5, 4])

        self.heap.clear()
        for val in [4, 4, 2, 2, 1]:
            self.heap.push(val)
        self.assertEqual(self.heap.heap_sort(), [1, 2, 2, 4, 4])
        self.assertEqual(self.heap.to_list(), [1, 2, 4, 4, 2])

        self.heap.clear()
        for val in [1, 2, 3, 4, 5]:
            self.heap.push(val)
        self.assertEqual(self.heap.heap_sort(), [1, 2, 3, 4, 5])
        self.assertEqual(self.heap.to_list(), [1, 2, 3, 4, 5])

        self.heap.clear()
        for val in [5, 4, 3, 2, 1]:
            self.heap.push(val)
        self.assertEqual(self.heap.heap_sort(), [1, 2, 3, 4, 5])
        self.assertEqual(self.heap.to_list(), [1, 2, 4, 5, 3])

        self.heap.clear()
        self.heap.push(42)
        self.assertEqual(self.heap.heap_sort(), [42])

        self.heap.clear()
        self.assertEqual(self.heap.heap_sort(), [])


    def test_build_heap(self):
        heap = MinHeap.build_heap("9831")
        self.assertEqual(heap.to_list(), ['1', '8', '3', '9'])
        self.assertEqual(heap.size(), 4)
        heap = MinHeap.build_heap(['d', 'a', 'c', 'b'])
        self.assertEqual(heap.heap_sort(), ['a', 'b', 'c', 'd'])

        test_cases = [
            ({6, 1, 3}, [1, 3, 6]), # 집합
            ((5, 2, 7, 4), [2, 4, 7, 5]),
            (range(5, 0, -1), [1, 2, 3, 5, 4]),
            ([], []),
        ]
        for iterable, expected_heap in test_cases:
            heap = MinHeap.build_heap(iterable)
            self.assertEqual(heap.to_list(), expected_heap)
            heap.push(0)
            self.assertEqual(heap.peek(), 0)
            self.assertEqual(heap.pop(), 0)
            self.assertEqual(heap.size(), len(expected_heap))


    def test_replace_and_try_pushpop(self):
        for val in [4, 7, 2, 9, 5]:
            self.heap.push(val)
        self.assertEqual(self.heap.peek(), 2)
        self.heap.replace_root(6)
        self.assertEqual(self.heap.peek(), 4)
        self.heap.replace_root(1)
        self.assertEqual(self.heap.peek(), 1)

        result = self.heap.try_pushpop(0)
        self.assertEqual(result, 0)
        self.assertEqual(self.heap.peek(), 1)
        result = self.heap.try_pushpop(10)
        self.assertEqual(result, 1, "기존 최소값 반환")
        self.assertIn(10, self.heap.heap, "10은 힙에 들어감")
        result = self.heap.try_pushpop(4)
        self.assertEqual(result, 4)
        self.assertNotIn(4, self.heap.heap)

        empty_heap = MinHeap()
        self.assertIsNone(empty_heap.replace_root(5))
        self.assertIsNone(empty_heap.try_pushpop(3))

        # 튜플 테스트
        tuple_heap = MinHeap()
        tuple_heap.push((2, "banana"))
        tuple_heap.push((1, "apple"))
        tuple_heap.replace_root((3, "cherry"))
        self.assertEqual(tuple_heap.peek(), (2, "banana"))

        result = tuple_heap.try_pushpop((2, "apple"))
        self.assertEqual(result, (2, "apple"))
        self.assertEqual(tuple_heap.peek(), (2, "banana"))


if __name__ == '__main__':
    unittest.main()
