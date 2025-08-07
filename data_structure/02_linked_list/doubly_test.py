from doubly_linked_list import Node, DoublyLinkedList

def make_dll(values):
    dll = DoublyLinkedList()
    for val in values:
        dll.push_back(val)
    return dll

def test_push_and_pop():
    dll = make_dll([10, 20, 30])
    assert str(dll) == "10 ⇆ 20 ⇆ 30"

    dll.push_front(5)
    assert str(dll) == "5 ⇆ 10 ⇆ 20 ⇆ 30"

    front = dll.pop_front()
    back = dll.pop_back()
    assert front == 5
    assert back == 30
    assert str(dll) == "10 ⇆ 20"
    print("push/pop test 통과")


def test_insert_search_delete():
    dll = make_dll([1, 2, 3])
    node2 = dll.search(2)
    dll.insert(node2, 99)
    assert str(dll) == "1 ⇆ 99 ⇆ 2 ⇆ 3"

    found = dll.search(3)
    assert found.key == 3

    deleted = dll.delete(dll.search(99))
    assert deleted == 99
    assert str(dll) == "1 ⇆ 2 ⇆ 3"
    print("insert/search/delete test 통과")


def test_size_empty_clear():
    dll = make_dll([7, 8, 9])
    assert dll.size() == 3 and not dll.is_empty()

    dll.clear()
    assert dll.size() == 0 and dll.is_empty()
    assert str(dll) == ""
    print("size/empty/clear test 통과")


def test_move_after_before():
    dll = make_dll([1, 2, 3, 4, 5])
    dll.move_after(dll.search(2), dll.search(4))
    assert str(dll) == "1 ⇆ 3 ⇆ 4 ⇆ 2 ⇆ 5"

    dll = make_dll([10, 20, 30, 40, 50])
    dll.move_before(dll.search(50), dll.search(10))
    assert str(dll) == "50 ⇆ 10 ⇆ 20 ⇆ 30 ⇆ 40"

    dll = make_dll([99])
    dll.move_after(dll.search(99), dll.search(99))
    assert str(dll) == "99"

    dll = make_dll([1, 2, 3])
    c = dll.search(3)
    dll.move_before(c, c)
    assert str(dll) == "1 ⇆ 2 ⇆ 3"

    print("move_after/before test 통과")


def test_splice():
    # 1) 단일 노드
    A = make_dll([1, 2, 3, 4, 5])
    B = make_dll([6, 7])
    B.splice(A.search(3), A.search(3), B.tail.prev)
    assert str(A) == "1 ⇆ 2 ⇆ 4 ⇆ 5"
    assert str(B) == "6 ⇆ 7 ⇆ 3"

    # 2) 연속 구간
    B.splice(A.search(2), A.search(4), B.search(7))
    assert str(A) == "1 ⇆ 5"
    assert str(B) == "6 ⇆ 7 ⇆ 2 ⇆ 4 ⇆ 3"

    # 3) 전체 (B → A)
    A.splice(B.head.next, B.tail.prev, A.tail.prev)
    assert str(A) == "1 ⇆ 5 ⇆ 6 ⇆ 7 ⇆ 2 ⇆ 4 ⇆ 3"
    assert str(B) == ""
    assert B.is_empty()

    # 4) start와 end가 서로 다른 리스트에 속해 있는 경우
    A = make_dll([1, 2, 3])
    B = make_dll([4, 5, 6])
    B.splice(A.search(2), B.search(5), B.search(4))  # 잘못된 splice
    assert str(A) == "1 ⇆ 2 ⇆ 3"
    assert str(B) == "4 ⇆ 5 ⇆ 6"

    # 5) after가 splice 구간 안에 있는 경우
    A.splice(A.search(1), A.search(3), A.search(2))  # after가 구간 내부
    assert str(A) == "1 ⇆ 2 ⇆ 3"

    # 6) start → end 구간이 끊겨 있는 경우
    node2 = A.search(2)
    node3 = A.search(3)
    node2.next = None  # 연결 끊기
    node3.prev = None
    B.splice(node2, node3, B.search(4))
    assert str(B) == "4 ⇆ 5 ⇆ 6"

    print("splice test 통과")


def test_reverse1():
    dll1 = make_dll([10, 20, 30, 40])
    dll1.reverse1()
    assert str(dll1) == "40 ⇆ 30 ⇆ 20 ⇆ 10"

    dll2 = make_dll([99])
    dll2.reverse1()
    assert str(dll2) == "99"
    print("reverse1 test 통과")


def test_edge_cases():
    dll = DoublyLinkedList()
    # 빈 리스트에서 노드 삭제 시도
    assert dll.pop_front() is None
    assert dll.pop_back() is None
    # head 앞에 값 삽입 시도(잘못된 위치)
    assert dll.insert(dll.head, 99) is False
    # 리스트에 없는 노드 삭제
    assert dll.delete(Node(999)) is None
    # 중복 키 검색
    dll = make_dll([1, 2, 1])
    assert dll.search(1).key == 1
    print("edge cases test 통과")


if __name__ == "__main__":
    test_push_and_pop()
    test_insert_search_delete()
    test_size_empty_clear()
    test_move_after_before()
    test_splice()
    test_reverse1()
    test_edge_cases()
