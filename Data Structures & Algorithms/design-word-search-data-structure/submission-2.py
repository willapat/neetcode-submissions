class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        def helper(node, index):
            if index == len(word):
                return node.isEndOfWord
            if word[index] != ".":
                if word[index] not in node.children:
                    return False
                return helper(node.children[word[index]], index + 1)
            else:
                for val in node.children:
                    if helper(node.children[val], index + 1):
                        return True
                return False

        return helper(self.root, 0)



