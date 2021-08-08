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
def find_duplicate_II(elements, k=None, approach=1):
    len_ele = len(elements)
    if not k:
        k = len_ele
    """
    Complexity

    1) Time: O(N) as each element is traversed and O(1) for accessing elements
    2) Space: O(N) due to use of hash tables
    """
    if approach == 1:
        index_dict =  {} # how much space 
        arr = [] # how much space does this array occupies ?
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
    
    elif approach == 2:
        """
        1)  Changing the  
        """
        if k <= 0:
            return False
        # if the range exceeds the given length of array then restrict to `k` or take the length of the array as `k`
        k = min(k, len_ele)

        uniq_elements = dict()
        """
        1)  Dividing the search in 2 methods 
            1)  first search from i to k 
            2)  second search from k to n 
        2)  Complexity
            1)  Space: O(K) as set holds only the elements based on `k` position
            2)  Time: O(K) as the traversal happens only within the specified `k` position
        """
        for i in range(k):
            if elements[i] in uniq_elements:
                return True
            uniq_elements[elements[i]] = i

        for i in range(k, len_ele):
            if elements[i] in uniq_elements:
                return True
            uniq_elements[elements[i]] = i

    elif approach == 3:
        if len(set(elements)) == len_ele:
            return False
        for i in range(len_ele):
            range_of_elements = elements[i: i+k+1]
            if len(set(range_of_elements)) < len(range_of_elements):
                return True
        return False

    else:
        pass

    return False


# print(find_duplicate_II([1,2,3,1], 3, 2))
# print(find_duplicate_II([1,0,1,1],3,2))
# print(find_duplicate_II([1,2,3,1,2,3], 2, 2)) # return False
# print(find_duplicate_II([1, 0, 1, 1], 1, 3)) # return True
# print(find_duplicate_II([1,2,3,1,2,3], 2, 3))