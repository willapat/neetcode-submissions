class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #add vals to a deque, remove vals if larger value being added then shift by 1 position
        #then we add the rightmost val to the result array
        dq = deque()
        res = []
        left, right = 0, 0
        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            
            if dq[0] < left:
                     dq.popleft()

            if (right - left + 1) >= k:
                res.append(nums[dq[0]])
                left += 1
            right += 1
        return res
              
            
