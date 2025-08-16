# 🌳 Binary Search Tree 

이 프로젝트는 두 가지 버전의 Binary Search Tree(BST)를 제공합니다:

1. **BST** – 중복 값을 허용하지 않는 기본 BST
2. **BSTWithCounter** – 중복 허용 BST <br>
(`BST` 클래스를 상속받아 삽입, 삭제, 순회 연산을 중복 처리에 맞게 오버라이딩했습니다. <br>
각 키의 개수는 `defaultdict`를 사용해 관리합니다.)

## 📁 폴더 구조
````
binary_search_tree/ 
├── bst.py              # 두 종류의 BST 구현 (BST, BSTWithCounter)
├── bst_examples.py     # 기본 BST 활용 예제 
├── test_bst.py         # BST 테스트 
└── test_examples.py    # 예제 테스트
````

## 📄 `bst_examples.py` : BST 예제 모음
| 이름                           | 설명                                           | 참고 문제                                                                                                |
|------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| `lowest_common_ancestor`     | BST에서 두 노드의 가장 가까운 공통 조상을 반환                 | [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)        |
| `kth_smallest`               | BST에서 k번째로 작은 원소를 반환                         | [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)                         |
| `path_sum_list`              | 루트부터 리프까지의 경로 중 합이 k인 모든 경로를 반환              | [LeetCode 113](https://leetcode.com/problems/path-sum-ii/)                                           |
| `path_sum_count`             | 트리 내 모든 경로 중 합이 k인 경로의 개수를 반환                | [LeetCode 437](https://leetcode.com/problems/path-sum-iii/)                                          |
| `BSTIterator` *(class)*      | BST를 중위 순회(Inorder Traversal)하는 이터레이터 클래스    | [LeetCode 173](https://leetcode.com/problems/binary-search-tree-iterator/)                           |
| `recover_tree`               | 두 노드가 바뀐 BST를 복구                             | [LeetCode 99](https://leetcode.com/problems/recover-binary-search-tree/)                             |
| `sorted_list_to_bst`         | 정렬된 리스트를 균형 이진 탐색 트리(BST)로 변환                | [LeetCode 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/) |
| `is_balanced`	               | 이진 트리가 균형 잡혀 있는지 확인                          |[LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/description/)
| `Codec` *(class)*            | 트리를 문자열로 직렬화`serialize()`, 복원`deserialize()` | [LeetCode 449](https://leetcode.com/problems/serialize-and-deserialize-bst/)                         |
| `convert_bst_to_greater`     | 각 노드의 값을 그 자신보다 큰 모든 노드 값의 합으로 바꾸기           | [LeetCode 538](https://leetcode.com/problems/convert-bst-to-greater-tree/)                           |
| `find_successor_predecessor` | 주어진 노드의 successor(후속자)와 predecessor(선행자) 반환  | -                                                                                                    |

<br>모든 예제는 직접 구현한 `BST` 클래스를 활용해 트리를 구성한 뒤, <br> 
BST 인스턴스 또는 루트 노드(root)를 인자로 받아 동작합니다. <br>
`find_successor_predecessor`를 제외한 예제들은 LeetCode를 참고했습니다.

---
### 업데이트 이력
- 2025.08.16 : BST 활용 예제 추가
- 2025.08.10 : 기본 BST 및 BSTWithCounter 구현