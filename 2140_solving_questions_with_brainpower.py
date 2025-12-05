class Solution(object):
    def mostPonits(self, questions):
        """

        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [q[0] for q in questions]

        for i in range(n-2, -1, -1):
            if (i + questions[i][1]+1) > n -1:
                dp[i] = max(dp[i], dp[i+1])
            else:
                dp[i] = max((dp[i] + dp[i + questions[i][1] +1 ]), dp[i+1])
        return dp[0]

questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
res = Solution()
result = res.mostPonits(questions)
print(result)
        
