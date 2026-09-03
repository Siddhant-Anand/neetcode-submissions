class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            d[i] = d.setdefault(i, 0) + 1

        top = max(d.values())

        buck_sort = [[] for _ in range(top)]

        for i, j in d.items():
            buck_sort[j - 1].append(i)

        ans = []

        for i in range(len(buck_sort) - 1, -1, -1):
            for j in buck_sort[i]:
                ans.append(j)

                if len(ans) == k:
                    return ans
