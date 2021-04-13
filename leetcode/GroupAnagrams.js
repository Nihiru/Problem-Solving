/***
 * Approach 1
 * Time complexity : O(N K log K ) where N is the length of string, K is the maximum length of a string in `words`.
 *                  The outer loop has a complexity O(N). Then, we sort each string in O(K log K) time
 * Space complexity : O(N K), the total information content stored in `uniqueWords`
 * 
 *  */

var groupAnagrams = function (words) {
    let uniqueWords = {}
    if (words.length) {
        // use a 2D array for storing the result
        words.forEach(word => {
            let current = word;
            let sortedWord = current.split('').sort().join('')
            if (!(sortedWord in uniqueWords)) {
                uniqueWords[sortedWord] = []
                uniqueWords[sortedWord].push(word)
            } else {
                uniqueWords[sortedWord].push(word)
            }

        });
    }
    return Object.values(uniqueWords)
}

console.log(groupAnagrams(["hello", "elloh", "world", "rowld", "SUP", "calling"]))

// approach 2
