import singly_linked_list
import singly_examples as se


def make_sll(values):
    sll = singly_linked_list.SinglyLinkedList()
    for val in values:
        sll.push_back(val)
    return sll



# ==== 클래스 기능 테스트 =========================

def test_insert_and_delete():
    ll = make_sll([1,2,3])
    ll.insert(2, 99)  # 1 → 2 → 99 → 3
    ll.insert(4, 30)  # 1 → 2 → 99 → 3 → 30
    ll.push_back(5)
    ll.push_back(6)
    assert str(ll) == "1 → 2 → 99 → 3 → 30 → 5 → 6"
    assert ll.delete(2) == 99   # 99 삭제
    assert str(ll) == "1 → 2 → 3 → 30 → 5 → 6"
    assert ll.pop_front() == 1
    assert ll.pop_back() == 6
    assert ll.delete_node(ll.search(5)) == 5
    assert str(ll) == "2 → 3 → 30"
    assert ll.size() == 3
    print("insert push delete pop test 통과")


def test_is_empty_and_clear():
    ll = make_sll([1,2,3])
    assert not ll.is_empty()
    ll.clear()
    assert ll.is_empty()
    assert str(ll) == ""
    print("clear, is_empty test 통과")


def test_reverse():
    ll = make_sll([1, 2])
    ll.reverse1()
    assert str(ll) == "2 → 1"
    ll = make_sll([1,2,3,4,5])
    ll.reverse1()
    assert str(ll) == "5 → 4 → 3 → 2 → 1"
    print("reverse test 통과")



# ==== 예제 테스트 ==========================

def test_delete_duplicates():
    # 모든 노드가 동일한 key값을 가지는 경우
    assert str(se.delete_duplicates(make_sll([1, 1, 1, 1, 1]))) == "1"
    # 중복 없음
    assert str(se.delete_duplicates(make_sll([1, 2, 3, 4, 5]))) == "1 → 2 → 3 → 4 → 5"
    # 빈 sll
    assert str(se.delete_duplicates(make_sll([]))) == ""
    # 노드 1개
    assert str(se.delete_duplicates(make_sll([1]))) == "1"
    # 복합
    assert str(se.delete_duplicates(make_sll([1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6]))) == "1 → 2 → 3 → 4 → 5 → 6"
    print("delete_duplicates test 통과")


def test_remove_kth_node_from_end():
    assert str(se.remove_kth_node_from_end(make_sll([1, 2, 3, 4, 5]), 2)) == "1 → 2 → 3 → 5"  # 기본
    assert str(se.remove_kth_node_from_end(make_sll([10, 20, 30]), 3)) == "20 → 30"  # 맨 앞 삭제
    assert str(se.remove_kth_node_from_end(make_sll([7, 8, 9]), 7)) == "7 → 8 → 9"  # k > 길이
    assert str(se.remove_kth_node_from_end(make_sll([100]), 1)) == ""  # 마지막 삭제
    assert str(se.remove_kth_node_from_end(make_sll([]), 2)) == ""  # 빈 리스트
    print("get_kth_node_from_end test 통과")


def test_merge_two_sorted_lists():
    assert str(se.merge_two_sorted_lists(make_sll([]), make_sll([]))) == ""  # 둘 다 빈 리스트
    assert str(se.merge_two_sorted_lists(make_sll([1, 3, 5]), make_sll([]))) == "1 → 3 → 5"  # 하나만 있는 경우
    assert str(se.merge_two_sorted_lists(make_sll([2, 4, 6]), make_sll([1, 2, 2, 4]))) == "1 → 2 → 2 → 2 → 4 → 4 → 6"
    assert str(se.merge_two_sorted_lists(make_sll([1, 4, 7]), make_sll([2, 3, 5, 6]))) == "1 → 2 → 3 → 4 → 5 → 6 → 7"
    print("merge_two_sorted_lists test 통과")


def test_detect_cycle():
    # 1. 순환 없는 리스트
    sll = make_sll([1, 2, 3, 4])
    assert se.detect_cycle(sll) is None
    # 2. 자기 자신을 가리키는 순환 (노드 1개)
    sll2 = make_sll([10])
    node = sll2.head.next
    node.next = node
    assert se.detect_cycle(sll2) == node
    # 3. 마지막 노드가 중간 노드를 가리키는 순환
    sll3 = make_sll([1, 2, 3, 4, 5])
    first = sll3.head.next
    second = first.next
    third = second.next
    fourth = third.next
    fifth = fourth.next
    fifth.next = second # 5 → 2 로 순환
    assert se.detect_cycle(sll3) == second
    # 4. 빈 리스트
    assert se.detect_cycle(make_sll([])) is None
    # 5. 노드 하나, 순환 없음
    assert se.detect_cycle(make_sll([99])) is None
    print("detect_cycle test 통과")


def test_is_palindrome():
    # 회문인 경우 (홀수 길이)
    assert se.is_palindrome(make_sll([1, 2, 3, 4, 5, 4, 3, 2, 1])) is True
    # 회문인 경우 (짝수 길이)
    assert se.is_palindrome(make_sll([1, 2, 1, 3, 3, 1, 2, 1])) is True
    # 회문 아님
    assert se.is_palindrome(make_sll([1, 2, 3, 1, 4])) is False
    # 길이 2
    assert se.is_palindrome(make_sll([5, 6])) is False
    # 길이 1 (항상 회문)
    assert se.is_palindrome(make_sll([7])) is True
    # 빈 리스트 (회문으로 간주)
    assert se.is_palindrome(make_sll([])) is True
    print("is_palindrome test 통과")


def test_reorder_list():
    # 짝수 길이
    assert str(se.reorder_list(make_sll([1, 2, 2, 4]))) == "1 → 4 → 2 → 2"
    # 홀수 길이
    assert str(se.reorder_list(make_sll([1, 2, 3, 4, 5]))) == "1 → 5 → 2 → 4 → 3"
    # 노드 1개
    assert str(se.reorder_list(make_sll([99]))) == "99"
    # 빈 리스트
    assert str(se.reorder_list(make_sll([]))) == ""
    print("reorder_list test 통과")


def test_reverse_between():
    # 부분 뒤집기
    assert str(se.reverse_between(make_sll([1, 2, 3, 4, 5]), 2, 4)) == "1 → 4 → 3 → 2 → 5"
    # 전체 뒤집기
    assert str(se.reverse_between(make_sll([1, 2, 3, 4]), 1, 4)) == "4 → 3 → 2 → 1"
    # 첫 두 개만 뒤집기
    assert str(se.reverse_between(make_sll([10, 20, 30]), 1, 2)) == "20 → 10 → 30"
    # 끝 두 개만 뒤집기
    assert str(se.reverse_between(make_sll([7, 8, 9]), 2, 3)) == "7 → 9 → 8"
    # 하나만 뒤집기 (변화 없음)
    assert str(se.reverse_between(make_sll([5, 6, 7]), 2, 2)) == "5 → 6 → 7"
    # 노드 하나
    assert str(se.reverse_between(make_sll([1]), 1, 1)) == "1"
    # 빈 리스트
    assert str(se.reverse_between(make_sll([]), 1, 1)) == ""
    print("reverse_between test 통과")


def test_reverse_k_group():
    assert str(se.reverse_k_group(make_sll([1, 2, 3, 4]), 2)) == "2 → 1 → 4 → 3"
    assert str(se.reverse_k_group(make_sll([1, 2, 3, 4, 5, 6, 7]), 3)) == "3 → 2 → 1 → 6 → 5 → 4 → 7"
    assert str(se.reverse_k_group(make_sll([1, 2, 3, 4, 5]), 5)) == "5 → 4 → 3 → 2 → 1"
    assert str(se.reverse_k_group(make_sll([1, 3, 1]), 3)) == "1 → 3 → 1"
    assert str(se.reverse_k_group(make_sll([7, 8, 9]), 1)) == "7 → 8 → 9"
    assert str(se.reverse_k_group(make_sll([1, 2, 3]), 9)) == "1 → 2 → 3"
    assert str(se.reverse_k_group(make_sll([1]), 1)) == "1"
    assert str(se.reverse_k_group(make_sll([]), 2)) == ""
    print("reverse_k_group test 통과")


def test_rotate_right():
    assert str(se.rotate_right(make_sll([]), 5)) == ""
    assert str(se.rotate_right(make_sll([1]), 0)) == "1"
    assert str(se.rotate_right(make_sll([1, 2]), 1)) == "2 → 1"
    assert str(se.rotate_right(make_sll([1, 2, 3]), 3)) == "1 → 2 → 3"
    assert str(se.rotate_right(make_sll([5, 6, 7, 8, 9]), 7)) == "8 → 9 → 5 → 6 → 7"
    assert str(se.rotate_right(make_sll([10, 20, 30, 40]), 2)) == "30 → 40 → 10 → 20"
    assert str(se.rotate_right(make_sll([1, 3, 5, 7, 9, 11]), 3)) == "7 → 9 → 11 → 1 → 3 → 5"
    print("rotate_right test 통과")


def test_add_two_numbers():
    assert str(se.add_two_numbers(make_sll([7, 2, 4, 3]), make_sll([5, 6, 4]))) == "7 → 8 → 0 → 7"
    assert str(se.add_two_numbers(make_sll([9, 9]), make_sll([9, 9]))) == "1 → 9 → 8"
    assert str(se.add_two_numbers(make_sll([5]), make_sll([1, 9]))) == "2 → 4"
    assert str(se.add_two_numbers(make_sll([0]), make_sll([0]))) == "0"
    assert str(se.add_two_numbers(make_sll([6, 4, 6, 0, 4, 4, 9]),
                                  make_sll([3, 8, 7, 0, 3, 0, 1]))) == "1 → 0 → 3 → 3 → 0 → 7 → 5 → 0"
    assert str(se.add_two_numbers(make_sll([9, 9, 9, 9]), make_sll([1]))) == "1 → 0 → 0 → 0 → 0"

    print("add_two_numbers test 통과")


if __name__ == "__main__":
    print("▶ 클래스 기능 테스트")
    test_insert_and_delete()
    test_is_empty_and_clear()
    test_reverse()

    print("\n▶ 예제 테스트")
    test_delete_duplicates()
    test_remove_kth_node_from_end()
    test_merge_two_sorted_lists()
    test_detect_cycle()
    test_reorder_list()
    test_is_palindrome()
    test_reverse_between()
    test_reverse_k_group()
    test_rotate_right()
    test_add_two_numbers()