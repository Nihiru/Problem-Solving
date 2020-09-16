// Pattern for helper method recursion
function outer(input){
    var outerScopedVariable = []
    function helper(helperInput){
        helper(helperInput--)
    }

    helper(input)
    return outerScopedVariable
}

/**
 * 
 * @param {Array} arr  - from which odd or even are found
 */
function collectOddsValue(arr){
    let result = [];

    function helper(helperInput){
        if(helperInput.length === 0){
            return;
        }

        if(helperInput[0] %2 !== 0){
            // push only items that are odd
            result.push(helperInput[0])
        }
        // slicing array from the current position to the end of array 
        helper(helperInput.slice(1))
    }
    // calling inner recursive function
    helper(arr)
    return result;
}

console.log(collectOddsValue([1,2,3,4,5,6,7,8]))