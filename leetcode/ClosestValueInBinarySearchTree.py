"""
Complexity:
    Time:
        Average: O(Log(N))
        Worst: O(N)
    Space:
        Average: O(Log(N))
        Worst: O(N)
"""


def findClosestValueInBST_R(tree, target):
    return findClosestValueInBSTHelper_R(tree, target, float("inf"))


def findClosestValueInBSTHelper_R(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper_R(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper_R(tree.right, target, closest)
    else:
        return closest

# iterative implementation


"""
Complexity:
    Time:
        Average: O(Log(N))
        Worst: O(N)
    Space:
        Average: O(1)
        Worst: O(1)
"""


def findClosestValueInBST_I(tree, target):
    return findClosestValueInBSTHelper_I(tree, target, float("inf"))


def findClosestValueInBSTHelper_I(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
