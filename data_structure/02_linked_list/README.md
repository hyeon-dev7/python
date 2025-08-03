# 📁 02_linked_list
**단방향(Singly)** 및 **양방향(Doubly) 연결 리스트** 자료구조를 구현한 코드와 <br>
단방향 연결 리스트 관련 예제 풀이를 모아놓은 폴더입니다.
```
02_linked_list/
├── doubly_linked_list.py   # 양방향 연결 리스트 (Singly Linked List) 클래스 (구현 중)
├── singly_linked_list.py   # 단방향 연결 리스트 (Doubly Linked List) 클래스 구현
├── singly_examples.py      # 단방향 관련 예제 풀이 (LeetCode 참고)
└── singly_test.py          # 단방향 클래스 및 예제 테스트 코드
```
<br>

## 📄 `singly_examples.py` : 단방향 연결 리스트 예제 모음

| 함수명 | 설명                             | 참고 문제                                                                           |
|--------|--------------------------------|---------------------------------------------------------------------------------|
| `delete_duplicates` | 정렬된 리스트에서 중복 제거                | [LeetCode 83](https://leetcode.com/problems/remove-duplicates-from-sorted-list) |
| `remove_kth_node_from_end` | 뒤에서 k번째 노드 제거                  | [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list)   |
| `merge_two_sorted_lists` | 정렬된 두 리스트 병합                   | [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists)             |
| `detect_cycle` | 사이클 시작 노드 찾기                   | [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii)              |
| `reorder_list` | 노드 재배열 (L0 → Ln → L1 → Ln-1 …) | [LeetCode 143](https://leetcode.com/problems/reorder-list)                      |
| `is_palindrome` | 리스트의 회문 여부 확인                  | [LeetCode 234](https://leetcode.com/problems/palindrome-linked-list)            |
| `reverse_between`  | 특정 구간 뒤집기 (left ~ right)                   | [LeetCode 92](https://leetcode.com/problems/reverse-linked-list-ii) |
| `reverse_k_group`  | k개씩 뒤집기                                      | [LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group) |
| `rotate_right`     | 연결 리스트를 오른쪽으로 k만큼 회전               | [LeetCode 61](https://leetcode.com/problems/rotate-list)            |
| `add_two_numbers`  | 연결 리스트를 활용한 두 숫자의 덧셈               | [LeetCode 445](https://leetcode.com/problems/add-two-numbers-ii)    |
<br>모든 예제는 LeetCode 문제를 참고하였으나,          
LeetCode의 ListNode 구조가 아닌 직접 구현한 `SinglyLinkedList` 클래스를 기반으로 작성했습니다.       
더미 헤드를 포함하고 있기 때문에 LeetCode에 바로 제출할 수 있는 구조는 아닙니다.

---

### 현재 상태
`DoublyLinkedList` 구현 중이며, splice 연산에서 오류를 발견하여 수정 중입니다.       
  

---
### 업데이트 이력  
- 2025.08.03 : SLL 예제 추가(4개), README 수정 
- 2025.07.22 : 단방향 연결 리스트(SLL) 구현 및 예제 풀이, README 작성
