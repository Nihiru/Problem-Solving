/**
 * @param {interger} nums 
 */
var twoSum = function (target, nums) {
    result = []
    numbsObj = {}

    /**
     * O(N) time complexity and the space complexity is O(N)
     * */
    for (let num of nums) {
        // calculating the remainder
        let compliment = target - num;
        if (compliment in numbsObj) {
            result.push([num, compliment])
        }
        numbsObj[num] = 0
    }
    return result
}

/**
 * @param {integer} nums 
 * @returns list of triplets that sums upto 0
 * @description  The approach used here is to use a number and then access the next two ones byb adding the latter and finally adding
 * with former to get 0.
 */
var threeSum = function (nums) {
    /**
     * refer Dynamic type for structural typing
     */
    if (nums.constructor !== Array) {
        return "Illegal type passed"
    }
    output = []
    nums.sort((a, b) => a - b)
    for (var i = 0; i < nums.length - 2; i++) {
        if (i === 0 || (i > 0 && nums[i] != nums[i - 1])) {
            // 2 pointers are incremented/decremented to perform combinations on given ranges
            let low = i + 1
            let high = nums.length - 1
            // here 0 is the target and the complement defines the target for addition of 2 numbers  
            let sum = 0 - nums[i]
            // moving inward starting from the 2 pointers
            while (low < high) {
                // checking if the 2 points match the sum 
                if (nums[low] + nums[high] === sum) {
                    // match found 
                    output.push([nums[i], nums[low], nums[high]])
                    /**
                     * avoiding duplicates by changing the position of pointers 
                     * low < high : within a given range
                     * nums[low] === nums[low+1] : values of the starting pointer and the next pointer are one and the same 
                     *                             then increment pointer to next position
                     * nums[high] === nums[high -1]: values of ending pointer and the previous pointer are one and the same
                     *                               then decrement pointer to previous position
                     * 
                     * */
                    while (low < high && nums[low] === nums[low + 1])
                        low++;
                    while (low < high && nums[high] === nums[high - 1])
                        high--;
                    // both values at the pointers failed to achieve target sum thereby moving the pointers inwards
                    low++;
                    high--;
                }
                // due to sorting the right hand side will hold all the positive numbers, left hand side will hold all the negative numbers given that array is a sequence of integers
                else if (nums[low] + nums[high] > sum)
                    high--;
                else
                    low++;
            }
        }
    }
    return output
}

// console.log(twoSum(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
// console.log(threeSum([-4, -1, -1, 0, 1, 2]))
console.log(threeSum([-4, -2, -2, -1, -1, 0, 1, 2, 3, 4]))