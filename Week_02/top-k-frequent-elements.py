class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 字典（hashMap) 输入各个key 然后 value 是 频数 取最大的k 个
        n_f_dic={}
        for x in nums:
            if x not in n_f_dic:
                n_f_dic[x]=1
            else:
                n_f_dic[x]+=1
        f_n_dic={}
        for n,f in n_f_dic.items():
            if f not in f_n_dic:
                f_n_dic[f] = [n]
            else:
                f_n_dic[f].append(n)

        arr = []

        for x in range(len(nums),0,-1):
            if x in f_n_dic:
                for i in f_n_dic[x]:
                    arr.append(i)
        return arr[:k]
