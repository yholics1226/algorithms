# [Search a 2D Matrix] https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(matrix, target):
    n, m = len(matrix), len(matrix[0])
    lt, rt = 0, n*m-1
    while lt <= rt:
        mid = (lt + rt) // 2
        x = matrix[mid//m][mid%m]
        if x == target:
            return True
        elif x < target:
            lt = mid + 1
        else:
            rt = mid - 1
    return False
