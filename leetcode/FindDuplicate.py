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

print(find_duplicate([1,2,3,4,5,6], 3))