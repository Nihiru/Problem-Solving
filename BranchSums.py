'''
Binary sums:
    Description:
        To calculate the sum of a root node to the leaf on a branch.
    
    Complexity:
        Time: 
            - O(N) 
            - Traverse all the nodes in the tree
        Space: 
            - O(N)
            - Multiple recursive calls being made will be present in the call stack at once
    Return:
        The list of sums of all branches.
    
'''


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return
    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return

    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)
