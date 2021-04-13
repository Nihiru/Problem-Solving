from collections import defaultdict


def groupAnagrams(strs):
    """Transforming each string s into a character count, consisting of 26 non-negative integers representing the
    number of a's, b's, c's... These counts are used as hash keys and values represents the string in the array

    Args:
        strs (string): array of strings

    Returns:
        list(list): anagram lists
    """
    ans = defaultdict(list)
    for s in strs:
        # count of all characters from a-z
        count = [0] * 26
        for ch in s:
            # if character found change the occurence of it in count list
            count[ord(ch) - ord('a')] += 1
        # access the prop with key pointing to tuple of 26 items and its value the string
        ans[tuple(count)].append(s)
    return ans.values()
