class Solution {
  public:
    // Function to check if placing num at (row, col) is valid
    bool isValid(vector<vector<int>> &mat, int row, int col, int num) {
        int sr = (row / 3) * 3;
        int sc = (col / 3) * 3;

        for (int i = 0; i < 9; i++) {
            if (mat[row][i] == num) return false;                  // row
            if (mat[i][col] == num) return false;                  // col
            if (mat[sr + i / 3][sc + i % 3] == num) return false;  // 3x3 subgrid
        }
        return true;
    }

    bool solve(vector<vector<int>> &mat) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (mat[row][col] == 0) { // empty cell
                    for (int num = 1; num <= 9; num++) {
                        if (isValid(mat, row, col, num)) {
                            mat[row][col] = num;
                            if (solve(mat)) return true;
                            mat[row][col] = 0; // backtrack
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    // Function to find a solved Sudoku.
    void solveSudoku(vector<vector<int>> &mat) {
        solve(mat);
    }
};
