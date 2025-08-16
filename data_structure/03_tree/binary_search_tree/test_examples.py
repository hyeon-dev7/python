import unittest
from bst import BST
from bst_examples import *

class TestExamples(unittest.TestCase):

    def test_lowest_common_ancestor_all_cases(self):
        bst1 = BST()
        for i in [7, 3, 10, 2, 5, 9, 12]:
            bst1.insert(i)
        self.assertEqual(lowest_common_ancestor(bst1, bst1.root.left.left, bst1.root.right.right).key, 7)
        self.assertEqual(lowest_common_ancestor(bst1, bst1.root.left.left, bst1.root.left.right).key, 3)
        self.assertEqual(lowest_common_ancestor(bst1, bst1.root.right.left, bst1.root.right.right).key, 10)
        self.assertEqual(lowest_common_ancestor(bst1, bst1.root.left.right, bst1.root.left.right).key, 5)

        bst2 = BST()
        for i in [5, 3, 6, 2, 4, 1]:
            bst2.insert(i)
        self.assertEqual(lowest_common_ancestor(bst2, bst2.root.left.left.left, bst2.root.left.right).key, 3)

        bst3 = BST()
        self.assertIsNone(lowest_common_ancestor(bst3, bst2.root, bst2.root.left))

        bst4 = BST()
        for i in [15, 10, 20]:
            bst4.insert(i)
        external_node = TreeNode(99)  # not in tree
        result = lowest_common_ancestor(bst4, bst4.root.left, external_node)
        self.assertIsNone(result)


    def test_kth_smallest_all_cases(self):
        bst = BST()
        for i in [7, 3, 10, 2, 5, 9, 12]:
            bst.insert(i)
        root = bst.root
        self.assertEqual(kth_smallest(root, 1), 2)
        self.assertEqual(kth_smallest(root, 4), 7)
        self.assertEqual(kth_smallest(root, 7), 12)
        self.assertIsNone(kth_smallest(root, 100), 12)


    def test_path_sum_list(self):
        bst = BST()
        for i in [5, 4, 9, 11, 13, 7, 2, 1]:
            bst.insert(i)
        assert path_sum_list(bst.root, 12) == [[5, 4, 2, 1]]
        assert path_sum_list(bst.root, 21) == [[5, 9, 7]]
        assert path_sum_list(bst.root, 100) == []

        bst2 = BST()
        for i in [11, 9, 10, 4, 12, -1] :
            bst2.insert(i)
        result = path_sum_list(bst2.root, 23)
        expected = [[11, 9, 4, -1], [11, 12]]
        assert sorted(result) == sorted(expected)

        bst3 = BST()
        bst3.insert(5)
        assert path_sum_list(bst3.root, 5) == [[5]]

        bst4 = BST()
        for i in [10, 16, 7, 9, 5, 4]:
            bst4.insert(i)
        result = path_sum_list(bst4.root, 26)
        expected = [[10, 7, 5, 4], [10, 7, 9], [10, 16]]
        assert sorted(result) == sorted(expected)


    def test_path_sum_count(self):
        bst = BST()
        for i in [5, 3, 7, 2, 4, 8]:
            bst.insert(i)
        assert path_sum_count(bst.root, 8) == 2
        assert path_sum_count(bst.root, 12) == 2

        bst2 = BST()
        for i in [1, 2, 3]:
            bst2.insert(i)
        assert path_sum_count(bst2.root, 100) == 0

        bst3 = BST()
        bst3.insert(7)
        assert path_sum_count(bst3.root, 7) == 1
        assert path_sum_count(bst3.root, 4) == 0

        bst4 = BST()
        for i in [5, 3, -1, 4, 6]:
            bst4.insert(i)
        assert path_sum_count(bst4.root, 7) == 2
        assert path_sum_count(None, 0) == 0


    def test_bst_iterator(self):
        bst1 = BST()
        for i in [5, 3, 7, 2, 4, 6, 8]:
            bst1.insert(i)
        it1 = BSTIterator(bst1.root)
        result1 = []
        while it1.hasNext():
            result1.append(it1.next())
        assert result1 == [2, 3, 4, 5, 6, 7, 8]

        bst2 = BST()
        bst2.insert(10)
        it2 = BSTIterator(bst2.root)
        assert it2.hasNext() is True
        assert it2.next() == 10
        assert it2.hasNext() is False

        bst3 = BST()
        for i in [5, 4, 3, 2, 1]:
            bst3.insert(i)
        it3 = BSTIterator(bst3.root)
        result3 = []
        while it3.hasNext():
            result3.append(it3.next())
        assert result3 == [1, 2, 3, 4, 5]

        it4 = BSTIterator(None)
        assert it4.hasNext() is False


    def test_recover_tree(self):
        bst1 = BST()
        for i in [3, 1, 4, 2]:
            bst1.insert(i)
        bst1.search(2).key, bst1.search(3).key = 3, 2  # swap
        assert bst1.inorder() == [1, 3, 2, 4]
        assert recover_tree(bst1).inorder() == [1, 2, 3, 4]

        bst2 = BST()
        for i in [5, 3, 7, 2, 4, 8]:
            bst2.insert(i)
        bst2.search(5).key, bst2.search(2).key = 2, 5
        assert recover_tree(bst2).inorder() == [2, 3, 4, 5, 7, 8]

        bst3 = BST()
        for i in [10, 5, 15, 12]:
            bst3.insert(i)
        bst3.search(12).key, bst3.search(15).key = 15, 12
        assert recover_tree(bst3).inorder() == [5, 10, 12, 15]

        bst4 = BST()
        bst4.insert(42)
        assert recover_tree(bst4).inorder() == [42]

        bst5 = BST()
        for i in [20, 10, 30, 5, 15, 25, 35]:
            bst5.insert(i)
        bst5.search(5).key, bst5.search(35).key = 35, 5
        assert recover_tree(bst5).inorder() == [5, 10, 15, 20, 25, 30, 35]

        bst6 = BST()
        for i in [1, 2, 3, 4, 5]:
            bst6.insert(i)
        bst6.search(2).key, bst6.search(4).key = 4, 2
        assert recover_tree(bst6).inorder() == [1, 2, 3, 4, 5]


    def test_sorted_list_to_bst(self):
        assert sorted_list_to_bst([]) is None

        root = sorted_list_to_bst([3, 7])
        assert root.key == 3
        assert root.left is None
        assert root.right.key == 7

        root = sorted_list_to_bst([1, 2, 3])
        assert root.key == 2
        assert root.left.key == 1
        assert root.right.key == 3

        root = sorted_list_to_bst([10, 20, 30, 40])
        assert root.key == 20
        assert root.left.key == 10
        assert root.right.key == 30
        assert root.right.right.key == 40

        lst = list(range(1, 31))
        root = sorted_list_to_bst(lst)
        assert root.key == 15
        assert root.left.key == 7
        assert root.right.key == 23
        # 왼쪽 서브트리
        assert root.left.right.key == 11
        assert root.left.left.left.key == 1
        # 오른쪽 서브트리
        assert root.right.left.right.key == 21
        assert root.right.right.right.right.key == 30


    def test_is_balanced_all_cases(self):
        bst1 = BST()
        for i in [7, 3, 10, 2, 5, 9, 12]:
            bst1.insert(i)
        self.assertTrue(is_balanced(bst1.root))

        bst2 = BST()
        for i in [2, 1]:
            bst2.insert(i)
        self.assertTrue(is_balanced(bst2.root))

        bst3 = BST()
        for i in [1, 2, 3, 4, 5]:
            bst3.insert(i)
        self.assertFalse(is_balanced(bst3.root))

        bst4 = BST()
        for i in [10, 5, 15, 20, 25]:
            bst4.insert(i)
        self.assertFalse(is_balanced(bst4.root))


    def test_codec_serialize_deserialize(self):
        codec = Codec()

        bst1 = BST()
        for i in [7, 3, 10, 2, 5, 9, 12]:
            bst1.insert(i)
        data1 = codec.serialize(bst1.root)
        bst1.root = codec.deserialize(data1)
        self.assertEqual(bst1.preorder(), [7, 3, 2, 5, 10, 9, 12])
        self.assertEqual(codec.serialize(bst1.root), data1)

        bst2 = BST()
        for i in [1, 2, 3, 4, 5]:
            bst2.insert(i)
        data2 = codec.serialize(bst2.root)
        bst2.root = codec.deserialize(data2)
        self.assertEqual(bst2.preorder(), [1, 2, 3, 4, 5])
        self.assertEqual(codec.serialize(bst2.root), data2)

        bst3 = BST()
        for i in [5, 4, 3, 2, 1]:
            bst3.insert(i)
        data3 = codec.serialize(bst3.root)
        bst3.root = codec.deserialize(data3)
        self.assertEqual(bst3.preorder(), [5, 4, 3, 2, 1])
        self.assertEqual(codec.serialize(bst3.root), data3)

        bst4 = BST()
        bst4.insert(42)
        data4 = codec.serialize(bst4.root)
        self.assertEqual(data4, "42,None,None")
        bst4.root = codec.deserialize(data4)
        self.assertEqual(bst4.preorder(), [42])

        bst5 = BST()
        data5 = codec.serialize(bst5.root)
        self.assertEqual(data5, "None")
        bst5.root = codec.deserialize(data5)
        self.assertEqual(bst5.preorder(), [])

        bst6 = BST()
        for i in [7, 4, 12, 6]:
            bst6.insert(i)
        data6 = codec.serialize(bst6.root)
        self.assertEqual(data6, "7,4,12,None,6,None,None,None,None")
        bst6.root = codec.deserialize(data6)
        self.assertEqual(bst6.preorder(), [7, 4, 6, 12])


    def test_convert_bst_to_greater(self):
        bst1 = BST()
        for i in [7, 3, 10, 2, 5, 9, 12]:
            bst1.insert(i)
        self.assertEqual(convert_bst_to_greater(bst1).inorder(), [48, 46, 43, 38, 31, 22, 12])

        bst2 = BST()
        for i in [1, 2, 3, 4, 5]:
            bst2.insert(i)
        self.assertEqual(convert_bst_to_greater(bst2).inorder(), [15, 14, 12, 9, 5])

        bst3 = BST()
        for i in [5, 4, 3, 2, 1]:
            bst3.insert(i)
        self.assertEqual( convert_bst_to_greater(bst3).inorder(), [15, 14, 12, 9, 5])


    def test_find_successor_predecessor(self):
        bst = BST()
        for i in [5, 4, 9, 11, 13, 7, 2, 1]:
            bst.insert(i)

        successor, predecessor = find_successor_predecessor(bst, bst.search(5))
        assert successor.key == 7, f"Expected 7, got {successor.key}"
        assert predecessor.key == 4, f"Expected 4, got a {predecessor.key}"

        successor, predecessor = find_successor_predecessor(bst, bst.search(4))
        assert successor.key == 5, f"Expected 5, got {successor.key}"
        assert predecessor.key == 2, f"Expected 2, got {predecessor.key}"

        successor, predecessor = find_successor_predecessor(bst, bst.search(2))
        assert successor.key == 4, f"Expected 4, got {successor.key}"
        assert predecessor.key == 1, f"Expected 1, got {predecessor.key}"

        successor, predecessor = find_successor_predecessor(bst, bst.search(13))
        assert successor is None, f"Expected None, got {successor.key}"
        assert predecessor.key == 11, f"Expected 11, got {predecessor.key}"

        bst2 = BST()
        for i in [2, 3, 1, 4]:
            bst2.insert(i)

        successor, predecessor = find_successor_predecessor(bst2, bst2.search(3))
        assert successor.key == 4, f"Expected 4, got {successor.key}"
        assert predecessor.key == 2, f"Expected 2, got {predecessor.key}"

        successor, predecessor = find_successor_predecessor(bst2, bst2.search(1))
        assert successor.key == 2, f"Expected 2, got {successor.key}"
        assert predecessor is None, f"Expected None, got {predecessor.key}"

        bst_single = BST()
        bst_single.insert(10)
        successor, predecessor = find_successor_predecessor(bst_single, bst_single.root)
        assert successor is None and predecessor is None