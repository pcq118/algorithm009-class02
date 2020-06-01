
class Solution: 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() 
        res=[] 
        def backtrack(tem,tmp): 
            if not tem:
                res.append(tmp) 
                return 
            for i in range(len(tem)): 
                if i>0 and tem[i]==tem[i-1]:
                    continue 
                backtrack(tem[:i] + tem[i+1:],tmp + [tem[i]]) 
        backtrack(nums,[]) 
        return res