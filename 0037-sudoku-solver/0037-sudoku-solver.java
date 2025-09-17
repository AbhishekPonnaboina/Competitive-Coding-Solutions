class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        int n = 9;

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValid(board, num, r, c)) {
                            board[r][c] = num;

                            if (solve(board)) {
                                return true;
                            }

                            board[r][c] = '.'; // backtrack
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, char num, int r, int c) {
        int sr = (r / 3) * 3;
        int sc = (c / 3) * 3;

        for (int i = 0; i < 9; i++) {
            if (board[i][c] == num) return false;         // column check
            if (board[r][i] == num) return false;         // row check
            if (board[sr + i / 3][sc + i % 3] == num) return false; // 3x3 subgrid
        }
        return true;
    }
}
