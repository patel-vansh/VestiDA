# User function Template for python3

class Solution:

    def find_empty_cell(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    # Function to find a solved Sudoku.
    def SolveSudoku(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True  # The board is already filled, solution found!

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(board, num, row, col):
                board[row][col] = num
                if self.SolveSudoku(board):
                    return True
                board[row][col] = 0  # Backtrack and try the next number
        return False  # No solution found

    def is_valid(self, board, num, row, col):
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check column
        for j in range(9):
            if board[j][col] == num:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row + i][box_col + j] == num:
                    return False

        return True  # The number is valid in this cell

    # Function to print grids of the Sudoku.
    def printGrid(self, arr):
        for row in arr:
            for col in row:
                print(col, end=" ")
            print()


if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    ob = Solution()
    if ob.SolveSudoku(grid):
        ob.printGrid(grid)
    else:
        print("No Solution Exists")
    # t = int(input())
    # while t > 0:
    #     grid = [[0 for i in range(9)] for j in range(9)]
    #     row = [int(x) for x in input().strip().split()]
    #     k = 0
    #     for i in range(9):
    #         for j in range(9):
    #             grid[i][j] = row[k]
    #             k += 1
    #     ob = Solution()
    #     if ob.SolveSudoku(grid):
    #         ob.printGrid(grid)
    #         print()
    #     else:
    #         print("No Solution Exists")
    #     t = t - 1
