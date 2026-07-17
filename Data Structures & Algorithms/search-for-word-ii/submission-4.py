class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Solution:
    def __init__(self):
            self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isEndOfWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        for word in words:
            self.addWord(word)

        self.res = []

        def helper(node, i, j, word):
            if node.isEndOfWord:
                self.res.append(word)
                node.isEndOfWord = False
            if i + 1 < len(board) and board[i + 1][j] in node.children:
                letter = board[i + 1][j]
                board[i + 1][j] = 0
                helper(node.children[letter], i + 1, j, word + letter)
                board[i + 1][j] = letter
            if i - 1 >= 0 and board[i - 1][j] in node.children:
                letter = board[i - 1][j]
                board[i - 1][j] = 0
                helper(node.children[letter], i - 1, j, word + letter)
                board[i - 1][j] = letter
            if j + 1 < len(board[0]) and board[i][j + 1] in node.children:
                letter = board[i][j + 1]
                board[i][j + 1] = 0
                helper(node.children[letter], i, j + 1, word + letter)
                board[i][j + 1] = letter
            if j - 1 >= 0 and  board[i][j - 1] in node.children:
                letter = board[i][j - 1]
                board[i][j - 1] = 0
                helper(node.children[letter], i, j - 1, word + letter)
                board[i][j - 1] = letter
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                letter = board[i][j]
                if letter in self.root.children:
                    board[i][j] = 0
                    helper(self.root.children[letter], i, j, letter)
                    board[i][j] = letter
        return self.res
        
                    
        
        
        