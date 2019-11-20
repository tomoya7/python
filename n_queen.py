# -*- coding: utf-8 -*-
# 回溯法实现八皇后
class  Solution:
    def SolveNqueen(self,n):
        ans=[]
        def dfs (nums,row):
            if row==n:
                ans.append(nums[:])
                return
            for col in range(n):
                nums[row]=col
                if valid(nums,row):
                    dfs(nums,row+1)
        def valid(nums,row):
            for i in range(row):
                if nums[row]==nums[i] or abs(row-i)==abs(nums[row]-nums[i]):
                    return False
            return True
        dfs([None for _ in range(n)],0)
        result=[[] for _ in range(len(ans))]
        for i in range(len(ans)):
            for col in ans[i]:
                tmp='*'*n
                result[i].append(tmp[:col]+"Q"+tmp[col+1:])
        return result
if __name__ == '__main__':
    solution=Solution()
    result=solution.SolveNqueen(8)
    print("solution_nums is "+str(len(result)))
    for i in range(len(result[0])):
        print(result[1][i])
    
    
