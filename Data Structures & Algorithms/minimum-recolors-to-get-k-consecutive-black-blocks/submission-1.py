class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k
        res = float('inf')
        while right <= len(blocks):
            dic = Counter(blocks[left:right])
            print(dic)
            replace = k - dic['B']
            res = min(res, replace)
            right += 1
            left += 1

        return res