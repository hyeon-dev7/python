from bst import TreeNode

def lowest_common_ancestor(bst, node1, node2):
    """ BST에서 두 노드의 가장 가까운 공통 조상을 반환 (LeetCode 235 참고) """
    root = bst.root
    if bst.search(node1.key) is None or bst.search(node2.key) is None :
        return None
    def lca(root, node1, node2):
        if node1.key < root.key and node2.key < root.key :
            return lca(root.left, node1, node2)
        if node1.key > root.key and node2.key > root.key :
            return lca(root.right, node1, node2)
        else :
            return root
    return lca(root, node1, node2)


def kth_smallest(root, k):
    """ BST에서 k번째로 작은 원소를 반환 (LeetCode 230 참고)"""
    stck = []
    cnt = 0
    curr = root
    while curr or stck :
        while curr:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        cnt += 1
        if cnt == k:
            return curr.key
        curr = curr.right
    return None


def path_sum_list(root, k):
    """ 루트부터 리프까지의 경로 중 합이 k인 모든 경로를 반환 (LeetCode 113 참고) """
    if root is None :
        return []
    res =[]
    stck =[(root, root.key, [root.key])]
    while stck :
        curr, path_sum, path = stck.pop()
        if path_sum == k and curr.left is None and curr.right is None:
            res.append(path)
        if curr.left :
            stck.append((curr.left, path_sum+curr.left.key, path+[curr.left.key]))
        if curr.right:
            stck.append((curr.right, path_sum + curr.right.key, path+[curr.right.key]))
    return res


def path_sum_count(root, k):
    """트리 내 모든 경로 중 합이 k인 경로의 개수를 반환 (LeetCode 437 참고) """
    from collections import defaultdict

    def dfs(root, path_sum, prefix_sum) :
        if root is None:
            return 0
        path_sum += root.key
        cnt = prefix_sum[path_sum-k]
        prefix_sum[path_sum] += 1
        cnt += dfs(root.left, path_sum, prefix_sum)
        cnt += dfs(root.right, path_sum, prefix_sum)
        prefix_sum[path_sum] -= 1
        return cnt
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    return dfs(root,0, prefix_sum)



class BSTIterator:
    """BST를 중위 순회하는 이터레이터 클래스 (LeetCode 173 참고)"""
    def __init__(self, root):
        self.gen = self._inorder(root)
        self._next = next(self.gen, None)

    def _inorder(self, root):
        if root is None :
            return
        yield from self._inorder(root.left)
        yield root.key
        yield from self._inorder(root.right)

    def next(self) -> int:
        """다음 원소를 반환"""
        res, self._next = self._next, next(self.gen, None)
        return res

    def hasNext(self) -> bool:
        """다음 원소의 존재 여부 반환"""
        return self._next is not None



def recover_tree(bst):
    """ 두 노드가 바뀐 bst 복구(LeetCode 99 참고) """
    stck = []
    curr = bst.root
    prev = None
    node1 = node2 = None
    while curr or stck :
        while curr :
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        if prev and prev.key > curr.key :
            if not node1 :
                node1 = prev
            node2 = curr
        prev = curr
        curr = curr.right

    if node1 and node2 :
        node1.key, node2.key = node2.key, node1.key
    return bst



def sorted_list_to_bst(lst):
    """ 정렬된 리스트를 균형 이진 탐색 트리(BST)로 변환 (LeetCode 108 참고) """
    return lst_to_bst_helper(lst, 0, len(lst)-1)

def lst_to_bst_helper(lst, left, right):
    if left > right:
        return None
    mid = (left+right)//2
    node = TreeNode(lst[mid])
    node.left = lst_to_bst_helper(lst, left, mid-1)
    node.right = lst_to_bst_helper(lst, mid+1, right)
    return node



def is_balanced(root):
    """ 이진 트리가 균형 잡혀 있는지 확인 (LeetCode 110 참고) """
    def check(root):
        if root is None :
            return 0
        l_height = check(root.left)
        r_height = check(root.right)
        if abs(l_height - r_height) > 1 :
            return -1
        if l_height == -1 or r_height == -1 :
            return -1
        return 1 + max(l_height, r_height)
    return check(root) != -1



from collections import deque

class Codec:
    def serialize(self, root) :
        """ Encodes a tree to a single string."""
        queue = deque([root])
        data = ""
        while queue :
            node = queue.popleft()
            if node :
                data += str(node.key) + ","
                queue.append(node.left)
                queue.append(node.right)
            else :
                data += 'None,'
        return data[:-1]

    def deserialize(self, data):
        """ Decodes encoded data to tree."""
        if not data :
            return None
        nodes = data.split(',')
        if nodes[0] == 'None':
            return None

        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue :
            curr = queue.popleft()
            if nodes[i] != 'None' :
                curr.left = TreeNode(int(nodes[i]))
                queue.append(curr.left)
            i += 1
            if nodes[i] != 'None' :
                curr.right = TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i += 1

        return root


def convert_bst_to_greater(bst):
    """ 각 노드의 값을 그 자신보다 큰 모든 노드 값의 합으로 바꾸기 (LeetCode 538 참고) """
    node = bst.root
    stck = []
    total = 0
    while node or stck :
        while node :
            stck.append(node)
            node = node.right
        node = stck.pop()
        total += node.key
        node.key = total
        node = node.left
    return bst



def find_successor_predecessor(bst, node):
    """ 주어진 노드의 successor(후속자)와 predecessor(선행자) 반환 """
    if node is None :
        return None, None

    # 후속자 찾기
    successor = None
    if node.right :
        successor = node.right
        while successor.left :
            successor = successor.left
    else :
        curr = bst.root
        while curr :
            if curr.key > node.key :
                successor = curr
                curr = curr.left
            elif curr.key < node.key :
                curr = curr.right
            else :
                break

    # 선행자 찾기
    predecessor = None
    if node.left :
        predecessor = node.left
        while predecessor.right :
            predecessor = predecessor.right
    else :
        curr = bst.root
        while curr :
            if curr.key > node.key :
                curr = curr.left
            elif curr.key < node.key :
                predecessor = curr
                curr = curr.right
            else :
                break

    return successor, predecessor