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
 * to solve this memoization is used where patterns are identified and reused in other parts of the a
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