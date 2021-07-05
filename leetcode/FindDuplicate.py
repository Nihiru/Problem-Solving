def find_duplicate(elements, approach):
    """
    Approach:
        Brute force

    Complexity:
    1) Time Complexity: O(N^2) due to traversing of array twice
    2) Space Complexity: O(1) as variables are utilized

    
    """ 
    len_ele = len(elements)
    uniq = 0
    if approach == 1:
        for i in range(len_ele):
            comp = elements[i]
            for j in range(i+1, len_ele):
                if elements[j] == comp:
                    uniq=True
                    break
    elif approach == 2:
        hash = {}
        for i in elements:
            if i in hash.keys():
                uniq = True
                break
            else:
                hash[i] = 0
    elif approach == 3:
        elements.sort()
        for i in range(len_ele-1):
            if elements[i] == elements[i+1]:
                uniq = True
    else:
        return "Unknown approach"
    if uniq:
        return True
    return False

# print(find_duplicate([1,2,3,4,5,6], 3))

"""
Description:
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

1)  finding out if duplicates exists in the given range `k`
2)  these ranges need to be apart for at least 1 position 
3)  and the elements need to be same based on the description

"""
def find_duplicate_II(elements, k, approach=0):
    len_ele = len(elements)
    index_dict =  {} # how much space 
    arr = [] # how much space does this array occupies ?
    """
    Complexity

    1) Time: O(N) as each element is traversed and O(1) for accessing elements
    2) Space: O(N) due to use of hash tables
    """
    for i in range(len_ele):
        if elements[i] in index_dict:
            index_dict[elements[i]] = (i - index_dict[elements[i]])
            arr.append(index_dict[elements[i]])
        else:
            index_dict[elements[i]] = i

    if len(arr):
        for ele in arr:
            if ele <= k:
                return True

    return False


print(find_duplicate_II([1,2,1,2], 2))