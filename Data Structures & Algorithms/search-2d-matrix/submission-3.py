class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            l, r = 0, len(matrix[mid]) - 1
            if target >= matrix[mid][l] and target <= matrix[mid][r]:
                while l <= r:
                    m = (l + r) // 2
                    if target == matrix[mid][m]:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    else:
                        l = m + 1

                return False
            elif target < matrix[mid][l]:
                right = mid - 1
            else:
                left = mid + 1
        return False
                