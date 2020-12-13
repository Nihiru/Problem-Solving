/**
 * Time complexity:
 * -) when recursive function is invoked the number of instructions it has to execute is increased i.e, 2^N
 * 
 * Space complexity: 
 * -) stack on the frame is inserted when a recursion occurs leading to O(n) space being occupied
 */
const dib = (n) => {
	if (n <= 1) return 1;
	dib(n - 1)
	dib(n - 1)
}

const lib = (n) => {
	if (n <= 1) return;
	lib(n - 2)
	lib(n - 2)
	/**
	 * as number of calls doubles down time complexity is O(2^n/2) => o(2^n) and 
	 * space complexity is O(n/2) => o(n)
	 */
}
/**
 * 
 * @param {int} n 
 * @description there is a limit on the number of stack frames being used 
 * to solve this memoization is used where patterns are identified and reused in other parts of
 * the problem
 */

const fib = (n, memo = {}) => {
	/**
	 * space complexity would accumulate to O(n)
	 * time complexity would accumlat to O(2n) => O(n) 
	 */
	if (n in memo) return memo[n]
	if (n <= 2) return 1;
	// memo is passed as "pass by reference"
	memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
	return memo[n]
}

console.log(fib(50))

/**
 * Grid Traveller
 * say that you're a traveller on 2D grid. You begin in the top left corner and your goal is to travel
 * to the bottom right corner. You may only move down or right.
 * m defines taking down side 
 * n defines taking right side
 */

const gridTraveller = (m, n, memo = {}) => {
	// Implementing memoization to identify reoccuring patterns along the way
	const key = m + '-' + n;

	/**
	 * find the key in memoization object
	 * here memoization concept is implemented through shared object that is propagated across function calls
	 *  */

	if (key in memo) return memo[key]

	// if 1x1 grid exists then there is no way to travel and return "Do Nothing" / "Zero" 
	if (m === 0 || n === 0) return 0;
	if (m === 1 && n === 1) return 1;
	/**
	 * (Brute force)
	 * Time complexity:
	 * Since each call to function depeneds on reducing 1 from either m or n. This yeilds to n+m
	 * As the call to function segregates in to 2 branches i.e, Binary tree this gives us O(2^(n+m))
	 * 
	 * Space complexity:
	 * It depends on the height of the tree i.e, n+m
	 * 
	 * (Efficient - Memoization)
	 * Time complexity:
	 * m * n -  m doesn't grow beyond m i.e, {0,...,m} and for same goes for n i.e, {0,...,n}
	 * 0 is base case as it travels all the way to 0 and then comes back to parent
	 * 
	 * Space complexity:
	 * Same as above
	 */
	memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
	return memo[key]
}

console.log(gridTraveller(2, 3))
console.log(gridTraveller(5, 5))
console.log(gridTraveller(18, 18)) // this would either crash or result in longer execution time if brute force used