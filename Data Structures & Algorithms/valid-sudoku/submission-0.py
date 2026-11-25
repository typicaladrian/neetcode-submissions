from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            In this problem, we are given a 9x9 sudoku board,
            defined as a 2D array of strings.

            Each value in the array is either a number 1-9, or "."
            for empty cell.

            Our goal is to check if the current board is valid
            using basic sudoku rules.

            A naive approach would be to iterate through the entire
            board, manually checking each row, column, and box.
           
            This approach is only naive in the sense that there is cleaner
            approach, because even with nested loops, our time complexity
            will always be O(9x9) which equates back to O(1). Generalizing
            though, we want to shoot for a time complexity better than O(n^3),
            which would be the time complexity for a brute force naive solution.

            The best way to write this would be to use a hashMap for each
            column, box, and row.

            This allows us to simply check if a value has already been seen in
            each, and if there is a value that has been seen already, then we instantly
            can mark the entire board as invalid, returning false.

            Of course the only thing that makes this a bit difficult is iterating through
            a 3x3 sub-box, but we can easily do this by converting our current i index
            to a 9x9 board coordinate, with our hashMap key being a tuple.

            So, defining our data structures:
                seenRow = defaultdict(set) --> key = row
                seenCol = defaultdict(set) --> key = column
                seenBox = defaultdict(set) --> key = coordinate tuple
        '''
        # instantiate our data structures
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenBox = defaultdict(set)

        # iterate through the entire board
        # check first all rows are valid
        for i in range(0, 9):
            for j in range(0, 9):
                # if current value is a ".", just skip
                if board[i][j] == ".":
                    continue

                currVal = int(board[i][j])
                # calculate current sub-box coordinates
                coord = (i // 3, j // 3)
                # full sweep check for duplicates
                if currVal in seenRow[j] or currVal in seenCol[i] or currVal in seenBox[coord]:
                    return False
                else:
                    seenRow[j].add(currVal)
                    seenCol[i].add(currVal)
                    seenBox[coord].add(currVal)
       
        return True 