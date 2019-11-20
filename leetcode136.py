# -*- coding: utf-8 -*-
# 只出现一次的数字
class Solution:
    def singleNumber(self,nums):
        ans=0
        for num in nums:
            ans =ans^num
        return ans
if __name__=="__main__":
    solution=Solution()
    ans=solution.singleNumber([2,2,1])
    print(ans)