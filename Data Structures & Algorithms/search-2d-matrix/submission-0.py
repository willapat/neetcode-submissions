class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = right - left // 2
            minVal = matrix[mid][0]
            maxVal = matrix[mid][len(matrix[mid]) - 1]
            if minVal == target or maxVal == target:
                return True
            elif target > maxVal:
                left = mid + 1
            elif target < minVal:
                right = mid - 1
            else:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    center = r - l // 2
                    if matrix[mid][center] == target:
                        return True
                    elif target > matrix[mid][center]:
                        l = center + 1
                    else:
                        r = center - 1
                
                return False
        return False