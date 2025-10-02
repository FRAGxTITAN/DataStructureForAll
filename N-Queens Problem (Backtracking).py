def solve_n_queens(n):
    solutions = []
    board = [-1]*n

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r]-col) == abs(r-row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row+1)

    backtrack(0)
    return solutions


# Example
print("N-Queens solutions for 4:", solve_n_queens(4))
