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