"""
트리 : 계층적 구조를 가지며, 부모-자식 관계를 통해 데이터를 조직적으로 표현할 수 있는 자료구조

이진 탐색 트리 (BST, binary search tree)
 - 모든 노드에 대해 왼쪽 서브트리의 값은 해당 노드보다 작고, 오른쪽 서브트리의 값은 해당 노드보다 큼
 - 중위 순회(inorder traversal) 시 항상 오름차순으로 정렬된 결과를 얻을 수 있음
 - 일반적으로 중복 값은 허용하지 않음 (구현에 따라 허용 가능 → 이 파일의 BSTWithCounter 클래스는 카운터 기반으로 중복 허용)

 시간 복잡도
  - 정렬된 데이터의 탐색, 삽입, 삭제 : 평균 O(log n)
  - 편향된 트리일 경우 성능 저하 (최악 O(n)) → 이를 방지하기 위해 균형 트리(예: AVL 트리, Red-Black 트리) 사용
 공간 복잡도
  - 노드 저장 공간 : O(n)
  - 재귀 호출 시 스택 공간 : O(h) (h: 트리의 높이)
"""

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _find_loc(self, value):
        """ value가 트리에 존재하면 해당 노드 반환,
        존재하지 않으면 삽입될 위치의 부모 노드를 반환 """
        if self.root is None:
            return None
        parent = None
        curr = self.root
        while curr:
            if curr.key == value:
                return curr
            elif curr.key > value:
                parent = curr
                curr = curr.left
            else:
                parent= curr
                curr = curr.right
        return parent

    def insert(self, value):
        """insert 후 해당 node 반환, 중복 값일 시 None 반환"""
        parent = self._find_loc(value)
        if parent is None or parent.key != value:
            node = TreeNode(value)
            if parent is None:
                self.root = node
            elif parent.key > value:
                parent.left = node
            else:
                parent.right = node
            return node
        else:
            return None

    def search(self, value) :
        """값이 트리에 존재하는지 확인, 있으면 해당 node, 없으면 None 반환 """
        node = self._find_loc(value)
        if node and node.key == value :
            return node
        return None


    def find_with_parent(self, value):
        parent = None
        curr = self.root
        while curr:
            if curr.key == value:
                return parent, curr
            elif curr.key > value:
                parent = curr
                curr = curr.left
            else :
                parent = curr
                curr = curr.right
        return None, None

    def delete(self, value):
        """ 해당 값을 트리에서 삭제 """
        parent, node = self.find_with_parent(value)
        if node is None :
            return None
        delete_value = node.key
        # 1: 리프 노드
        if node.left is None and node.right is None:
            if parent is None :
                self.root = None
            elif parent.left == node :
                parent.left = None
            else :
                parent.right = None
        # 2: 자식 하나
        elif node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if parent is None :
                self.root = child
            elif parent.left == node :
                parent.left = child
            else :
                parent.right = child
        # 3 : 자식 둘
        else :
            successor = self._get_successor(node)
            key = successor.key
            self.delete(key)
            node.key = key
        return delete_value

    def _get_successor(self, node):
        """내부 전용: 오른쪽 서브트리에서 가장 작은 노드"""
        def helper(node):
            if node and node.left :
                return helper(node.left)
            return node
        return helper(node.right)


    def preorder(self):
        """ 전위 순회 : Root → Left → Right 순으로 방문 """
        res = []
        def dfs(node):
            if node is None:
                return
            res.append(node.key)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
        return res

    def postorder(self):
        """ 후위 순회 : Left → Right → Root 순으로 방문 """
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.key)
        dfs(self.root)
        return res

    def inorder(self):
        """ 중위 순회 : Left → Root → Right 순으로 방문, BST에서는 오름차순으로 정렬된 결과 반환 """
        res,stck = [],[]
        curr = self.root
        while curr or stck:
            if curr :
                stck.append(curr)
                curr = curr.left
            else :
                curr = stck.pop()
                res.append(curr.key)
                curr = curr.right
        return res

    def levelorder(self):
        """ 레벨 순서 순회 : 루트부터 아래 방향으로 너비 우선 탐색(BFS) 수행 """
        if not self.root:
            return []
        res = []
        q = deque([self.root])
        while q :
            node = q.popleft()
            res.append(node.key)
            if node.left :
                q.append(node.left)
            if node.right :
                q.append(node.right)
        return res


    def count_nodes(self):
        """ 노드 개수 반환 """
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)
        return count(self.root)

    def height(self):
        """ 트리의 최대 깊이(높이) """
        def helper(node):
            if node is None :
                return 0
            return 1 + max(helper(node.left), helper(node.right))
        return helper(self.root)

    def find_min(self):
        """ 트리에서 가장 작은 값을 가진 노드 반환 (왼쪽 끝) """
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr

    def find_max(self):
        """ 트리에서 가장 큰 값을 가진 노드 반환 (오른쪽 끝) """
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr

    def is_valid_bst(self):
        """ 트리가 BST 조건을 만족하는지 확인 """
        def validate(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.key < max_val):
                return False
            return (validate(node.left, min_val, node.key) and
                    validate(node.right, node.key, max_val))
        return validate(self.root, float('-inf'), float('inf'))



from collections import defaultdict # 키 존재 여부 확인 없이 바로 값 증가 가능

class BSTWithCounter(BST):
    def __init__(self):
        super().__init__() # 부모 클래스(BST)의 초기화 실행
        self.counter = defaultdict(int)

    def insert(self, value):
        """ 중복 값일 경우 None 반환 후 counter +1 """
        node = super().insert(value)
        self.counter[value] += 1
        return node

    def delete(self, value):
        if self.counter[value] == 0:
            return None
        self.counter[value] -= 1
        if self.counter[value] == 0 :
            return super().delete(value)
        else :
            return value

    def get_count(self, value):
        """ 특정 value 값을 가지는 node 수 """
        return self.counter[value]

    def total_count(self):
        """ 중복을 고려한 전체 개수 """
        return sum(self.counter.values())

    def preorder(self):
        res = []
        def _preorder(node):
            if not node :
                return
            res.extend([node.key] * self.counter[node.key])
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        return res

    def postorder(self):
        res = []
        def _postorder(node):
            if not node :
                return
            _postorder(node.left)
            _postorder(node.right)
            res.extend([node.key] * self.counter[node.key])
        _postorder(self.root)
        return res

    def inorder(self):
        stck, res = [], []
        curr = self.root
        while curr or stck:
            while curr :
                stck.append(curr)
                curr = curr.left
            curr = stck.pop()
            res.extend([curr.key] * self.counter[curr.key])
            curr = curr.right
        return res

    def levelorder(self):
        if not self.root:
            return []
        res = []
        q = deque([self.root])
        while q :
            node = q.popleft()
            res.extend([node.key] * self.counter[node.key])
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res