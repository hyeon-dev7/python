import singly_linked_list

def delete_duplicates(sll):
    """중복 노드 제거 (LeetCode 83 참고)"""
    if sll.is_empty() :
        return ""
    curr = sll.head
    idx=0
    while curr.next :
        prev = curr
        curr = curr.next
        if prev.key == curr.key:
            sll.delete(idx)
            idx -= 1
        idx += 1

    return sll



def remove_kth_node_from_end(sll, k):
    """끝에서 k번째 노드 제거 (LeetCode 19 참고)"""
    if k > sll.size():
        return sll

    fast = sll.head
    for _ in range(k):
        fast = fast.next

    slow = sll.head
    while fast :
        fast = fast.next
        slow = slow.next
    sll.delete_node(slow)

    return sll



def merge_two_sorted_lists(l1, l2):
    """정렬된 두 연결 리스트 병합 (LeetCode 21 참고)"""

    merged = singly_linked_list.SinglyLinkedList()
    l1_curr = l1.head.next
    l2_curr = l2.head.next

    while l1_curr and l2_curr :
        if l1_curr.key <= l2_curr.key:
            merged.push_back(l1_curr.key)
            l1_curr = l1_curr.next
        else:
            merged.push_back(l2_curr.key)
            l2_curr = l2_curr.next

    while l1_curr :
        merged.push_back(l1_curr.key)
        l1_curr = l1_curr.next

    while l2_curr :
        merged.push_back(l2_curr.key)
        l2_curr = l2_curr.next

    return merged



def detect_cycle(sll):
    """ 사이클 시작 노드 반환 (플로이드의 토끼와 거북이) (LeetCode 142 참고)"""
    slow = sll.head
    fast = sll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None

    slow = sll.head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return fast



def reorder_list(sll):
    """ 연결 리스트 순서 재정렬 L0→Ln→L1→Ln-1→L2→... (LeetCode 143 참고)"""

    slow = sll.head
    fast = sll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow.next
    slow.next = None
    prev = None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first = sll.head.next
    second = prev
    while second :
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
    return sll


def is_palindrome(sll):
    """연결 리스트가 회문인지 확인 (LeetCode 234 참고)"""

    slow = sll.head
    fast = sll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = reverse_from(slow.next)

    front = sll.head.next
    back = slow.next
    while back:
        if front.key != back.key:
            return False
        front = front.next
        back = back.next
    return True

def reverse_from(node): # node부터 끝까지 뒤집기
    prev = None
    curr = node
    while curr:
        # next = curr.next
        # curr.next = prev
        # prev = curr
        # curr = next
        curr.next, prev, curr = prev, curr, curr.next
    return prev # reversed_head 리턴



def reverse_between(sll, left, right):
    """특정 구간 뒤집기 (LeetCode 92 참고)"""
    pass






