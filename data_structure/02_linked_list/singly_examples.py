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
    if sll.size()<right :
        return sll
    prev = sll.head
    for _ in range(1,left):
        prev = prev.next
    curr = prev.next.next
    tail = prev.next
    for _ in range(right - left):
        next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next
    tail.next = curr
    # print(sll)
    return sll



def reverse_k_group(sll, k):
    """ k개씩 뒤집기 (LeetCode 25 참고)"""
    if sll.head.next :
       sll.head.next = reverse_recursive(sll.head.next, k)
    return sll

def reverse_recursive(node, k):
    curr = node
    for _ in range(k):
        if curr is None :
            return node
        curr = curr.next
    prev = None
    curr = node
    for _ in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    node.next = reverse_recursive(curr, k)
    return prev



def rotate_right(sll, k):
    """연결 리스트를 오른쪽으로 k만큼 회전 (LeetCode 61)"""
    if sll.is_empty():
        return sll
    cnt = 1
    cur = sll.head.next
    while cur.next:
        cnt += 1
        cur = cur.next

    k = k % cnt
    if k == 0:
        return sll

    mid = sll.head
    for i in range(cnt - k):
        mid = mid.next
    new_mid = sll.head.next
    sll.head.next = mid.next
    mid.next = None
    cur.next = new_mid

    return sll


def add_two_numbers(l1, l2):
    """연결 리스트를 활용한 두 숫자의 덧셈 (LeetCode 445 참고)"""
    a = l1.head.next
    b = l2.head.next
    stck1 = []
    stck2 = []
    while a or b:
        if a:
            stck1.append(a.key)
            a = a.next
        if b:
            stck2.append(b.key)
            b = b.next
    c = 0
    res = singly_linked_list.SinglyLinkedList()
    while stck1 or stck2 or c == 1:
        if stck1 and stck2:
            x = stck1.pop()
            y = stck2.pop()
            z = (x + y + c) % 10
            c = (x + y + c) // 10

        elif stck1:
            x = stck1.pop()
            z = (x + c) % 10
            c = (x + c) // 10

        elif stck2:
            y = stck2.pop()
            z = (y + c) % 10
            c = (y + c) // 10
        else:
            z = 1
            c = 0
        res.push_front(z)
    return res

