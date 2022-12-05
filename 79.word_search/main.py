class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def search(r, c, index, letter_set):
            #print(r, c, index, letter_set)
            if index == len(word):
                return True
            elif r < 0 or r > len(board)-1:
                return False
            elif c < 0 or c > len(board[0])-1:
                return False
            elif board[r][c] != word[index]:
                return False
            elif (r, c) in letter_set:
                return False
            else:
                letter_set.add((r, c))
                a = search(r-1, c, index+1, letter_set)
                b = search(r+1, c, index+1, letter_set)
                e = search(r, c-1, index+1, letter_set)
                d = search(r, c+1, index+1, letter_set)
                letter_set.remove((r, c))
                return a or b or e or d
        
        letter_set = set()
        # These two lines of code below optimizes entire code
        # for certain scenarios. It will reduce the number of recursions
        # for the recursion tree.
        if word.count(word[0]) > word.count(word[-1]):
            word = word[::-1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0, letter_set):
                    return True
        return False

def main():
    solution = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(solution.exist(board, word))


    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(solution.exist(board, word))

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(solution.exist(board, word))

if __name__ == '__main__':
    main()