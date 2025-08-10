"""
unittest 테스트 러너가 클래스에서 'test_'로 시작하는 메서드 목록을 수집,
각 테스트 메서드마다 다음 과정을 수행

1. 새로운 테스트 인스턴스 생성
2. setUp() 호출 → 테스트 용 인스턴스 초기화, 각 테스트가 독립적으로 실행됨
3. 해당 test_ 메서드 실행
4. tearDown() 호출 (정리 작업이 필요한 경우)
"""

import unittest
from bst import BST, BSTWithCounter

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BST()

    def test_insert(self):
        self.assertIs(self.bst.insert(7),self.bst.root)
        self.assertIs(self.bst.insert(9),self.bst.root.right)
        self.assertIs(self.bst.insert(3),self.bst.root.left)
        self.assertIs(self.bst.insert(10),self.bst.root.right.right)
        self.assertIsNone(self.bst.insert(10))


    def test_delete(self):
        for i in [7, 3, 8, 1, 4, 10]:
            self.bst.insert(i)
        # 1. 존재하지 않는 노드 삭제 시도
        deleted_none = self.bst.delete(100)
        self.assertIsNone(deleted_none)
        # 2. 자식이 없는 노드(10) 삭제
        deleted_leaf = self.bst.delete(10)
        self.assertEqual(deleted_leaf, 10)
        # 3. 자식이 하나인 노드(3) 삭제
        self.assertEqual(self.bst.delete(3), 3)
        self.assertIsNone(self.bst.delete(3))
        # 4. 자식이 두 개인 노드(7) 삭제
        deleted_two_children = self.bst.delete(7)
        self.assertEqual(deleted_two_children, 7)
        self.assertIsNone(self.bst.search(7))
        self.assertEqual(self.bst.levelorder(), [8, 4, 1])

        bst2 = BST()
        for i in [50, 30, 70, 20, 40, 55, 60, 66, 80, 75, 57, 77]:
            bst2.insert(i)
        # 1: delete(70) → successor = 75 (has right child 77)
        self.assertEqual(bst2.delete(70), 70)
        self.assertEqual(bst2.root.right.key, 75)
        self.assertEqual(bst2.root.right.right.key, 80)
        self.assertEqual(bst2.root.right.right.left.key, 77)
        # 2: delete(30) → successor = 40 (no children)
        self.assertEqual(bst2.delete(30), 30)
        self.assertEqual(bst2.root.left.key, 40)
        self.assertEqual(bst2.root.left.left.key, 20)
        # 3: delete root → successor = 55 (has right child 60)
        self.assertEqual(bst2.delete(bst2.root.key), 50)
        self.assertEqual(bst2.height(), 4)
        self.assertEqual(bst2.root.key, 55)
        self.assertEqual(bst2.root.right.left.key, 60)
        self.assertEqual(bst2.root.right.left.left.key, 57)
        self.assertEqual(bst2.root.right.left.right.key, 66)
        self.assertEqual(bst2.inorder(), [20, 40, 55, 57, 60, 66, 75, 77, 80])


    def test_search(self):
        for v in [7, 3, 9]:
            self.bst.insert(v)
        found = self.bst.search(3)
        self.assertEqual(found.key, 3)

        missing = self.bst.search(100)
        self.assertIsNone(missing)


    def test_find_min_max(self):
        self.assertIsNone(self.bst.find_min())
        self.assertIsNone(self.bst.find_max())

        for i in [7, 9, 3, 1, 10]:
            self.bst.insert(i)

        self.assertEqual(self.bst.find_min().key, 1)
        self.assertEqual(self.bst.find_max().key, 10)

        n0 = self.bst.insert(0)
        n12 = self.bst.insert(12)
        self.assertIs(self.bst.find_min(), n0)
        self.assertIs(self.bst.find_max(), n12)


    def test_all_traversals(self):
        test_cases = [
            {
                "input": [], "inorder": [], "preorder": [], "postorder": [], "levelorder": []
            },
            {
                "input":      [10, 10, 5],
                "inorder":    [5, 10],
                "preorder":   [10, 5],
                "postorder":  [5, 10],
                "levelorder": [10, 5]
            },
            {
                "input":      [7, 9, 3, 1, 5, 12, 10],
                "inorder":    [1, 3, 5, 7, 9, 10, 12],
                "preorder":   [7, 3, 1, 5, 9, 12, 10],
                "postorder":  [1, 5, 3, 10, 12, 9, 7],
                "levelorder": [7, 3, 9, 1, 5, 12, 10]
            },
            {
                "input":      [8, 4, 12, 2, 6, 10, 14],
                "inorder":    [2, 4, 6, 8, 10, 12, 14],
                "preorder":   [8, 4, 2, 6, 12, 10, 14],
                "postorder":  [2, 6, 4, 10, 14, 12, 8],
                "levelorder": [8, 4, 12, 2, 6, 10, 14]
            },
            {
                "input":      [5, 3, 7, 2, 4, 6],
                "inorder":    [2, 3, 4, 5, 6, 7],
                "preorder":   [5, 3, 2, 4, 7, 6],
                "postorder":  [2, 4, 3, 6, 7, 5],
                "levelorder": [5, 3, 7, 2, 4, 6]
            }
        ]
        for case in test_cases:
            self.bst = BST()  # 새 트리 생성
            for i in case["input"]:
                self.bst.insert(i)
            self.assertEqual(self.bst.inorder(),    case["inorder"])
            self.assertEqual(self.bst.preorder(),   case["preorder"])
            self.assertEqual(self.bst.postorder(),  case["postorder"])
            self.assertEqual(self.bst.levelorder(), case["levelorder"])


    def test_count_height(self):
        test_cases = [
            {
                "input": [5, 3, 7, 2, 4, 6, 7],
                "count": 6, "height": 3
            },
            {
                "input": [10], "count": 1, "height": 1
            },
            {
                "input": [], "count": 0, "height": 0
            },
            {
                "input": [8, 4, 12, 2, 6, 10, 14],
                "count": 7, "height": 3
            }
        ]
        for case in test_cases:
            bst = BST()
            for i in case["input"]:
                bst.insert(i)
            assert bst.count_nodes() == case["count"]
            assert bst.height() == case["height"]

    def test_is_valid_bst(self):
        bst = BST()
        for v in [5, 3, 7, 2, 4, 6]:
            bst.insert(v)
        self.assertTrue(bst.is_valid_bst())

        bst.root.left.right.key = 6
        self.assertFalse(bst.is_valid_bst())



class TestBSTWithCounter(unittest.TestCase):
    def setUp(self):
        self.bst = BSTWithCounter()

    def test_insert_and_count(self):
        self.assertEqual(self.bst.insert(5), self.bst.root)
        self.assertIsNone(self.bst.insert(5))
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(3)
        self.assertEqual(self.bst.insert(1), self.bst.search(3).left)
        self.assertEqual(self.bst.insert(7), self.bst.root.right)

        self.assertEqual(self.bst.count_nodes(), 4)
        self.assertEqual(self.bst.total_count(), 7)
        self.assertEqual(self.bst.get_count(5), 3)
        self.assertEqual(self.bst.get_count(3), 2)
        self.assertEqual(self.bst.get_count(100), 0)


    def test_delete(self):
        bst = BSTWithCounter()
        for i in [5, 3, 1, 7, 7]:
            bst.insert(i)
        self.assertEqual(bst.delete(1), 1)
        self.assertIsNone(bst.delete(1))
        self.assertIsNone(bst.search(1))
        self.assertEqual(bst.get_count(1), 0)
        self.assertIsNone(bst.search(3).left)
        bst.delete(5)
        self.assertEqual(bst.root, bst.search(7))
        self.assertEqual(bst.root.left, bst.search(3))

        bst2 = BSTWithCounter()
        for v in [10, 5, 15, 3, 1, 4, 1, 7, 7, 12, 6]:
            bst2.insert(v)
        bst2.delete(7)
        self.assertEqual(bst2.delete(7), 7)
        self.assertIsNone(bst2.search(7))
        self.assertEqual(bst2.search(5).right, bst2.search(6))
        bst2.delete(1)
        bst2.delete(5)
        self.assertEqual(bst2.root.left, bst2.search(6))
        self.assertEqual(bst2.root.left.left, bst2.search(3))


    def test_traversals_with_duplicates(self):
        test_cases = [
            {
                "input":      [5, 5, 3, 3, 3, 7, 7],
                "inorder":    [3, 3, 3, 5, 5, 7, 7],
                "preorder":   [5, 5, 3, 3, 3, 7, 7],
                "postorder":  [3, 3, 3, 7, 7, 5, 5],
                "levelorder": [5, 5, 3, 3, 3, 7, 7]
            },
            {
                "input":      [10, 5, 3, 1, 4, 16, 12, 20, 20, 20],
                "inorder":    [1, 3, 4, 5, 10, 12, 16, 20, 20, 20],
                "preorder":   [10, 5, 3, 1, 4, 16, 12, 20, 20, 20],
                "postorder":  [1, 4, 3, 5, 12, 20, 20, 20, 16, 10],
                "levelorder": [10, 5, 16, 3, 12, 20, 20, 20, 1, 4]
            }
        ]
        for case in test_cases :
            bst = BSTWithCounter()  # 새 트리 생성
            for i in case["input"]:
                bst.insert(i)
            self.assertEqual(bst.inorder(),    case["inorder"])
            self.assertEqual(bst.preorder(),   case["preorder"])
            self.assertEqual(bst.postorder(),  case["postorder"])
            self.assertEqual(bst.levelorder(), case["levelorder"])


if __name__ == '__main__':
    unittest.main()