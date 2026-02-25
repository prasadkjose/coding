""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, n):
        """ Solution Method """
        # n =2, [[1,1][2]]
        # n=3, [[1,1,1], [1,2], [2,1]]
        # n=5, [[1,1,1,1,1], [2,1,1,1], [1,2,1,1], [1,1,2,1], [1,1,1,2], 
        # [2,2,1], [2,1,2], [1,2,2]] 1,1,2,3,5


        # The solution is the count of fibanacci.
        # Recursive with memoization
        cache = [-1] * (n + 1)
        # def fib(n: int) -> int:
        #     if n <= 2:
        #         return n

        #     if cache[n] != -1:
        #         return cache[n]

        #     cache[n] = fib(n - 1) + fib(n - 2)
        #     return cache[n]
        # return fib(n)

        # Iterative
        def iterative(n:int) -> int:
            if n<=2:
                return n
            
            prev1 = 1
            prev2 = 2
            # Move the window one step
            for _ in range(3, n+1):
                curr = prev1 + prev2
                prev1 = prev2
                prev2 = curr

            return prev2
        return iterative(n)

        # Formula
