# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_value = preorder.pop(0)
        for i in range(len(inorder)):
            if root_value == inorder[i]:
                root_index = i
                break
        root = TreeNode(root_value)
        temp = root
        def buildLandRTree(root,preorder,l_list,r_list):
            if len(l_list) == 0:
                root.left = None
            elif len(l_list) == 1:
                root.left = TreeNode(l_list[0])
            else:
                temp = []
                for i in range(len(l_list)):
                    temp.append(preorder.pop(0))
                temp_value = temp.pop(0)
                for i in range(len(l_list)):
                    if temp_value == l_list[i]:
                        temp_index = i
                        break
                temp_node = TreeNode(temp_value)
                buildLandRTree(temp_node,temp,l_list[:temp_index],l_list[temp_index+1:])
            if len(r_list) == 0:
                root.right = None
            elif len(r_list) == 1:
                root.right = TreeNode(r_list[0])
            else:
                temp = []
                for i in range(len(r_list)):
                    temp.append(preorder.pop(0))
                temp_value = temp.pop(0)
                for i in range(len(r_list)):
                    if temp_value == r_list[i]:
                        temp_index = i
                        break
                temp_node = TreeNode(temp_value)
                buildLandRTree(temp_node,temp,r_list[:temp_index],r_list[temp_index+1:])

        buildLandRTree(root,preorder,inorder[:root_index],inorder[root_index+1:])
