# 211. Design Add and Search Words Data Structure
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                node = node.children[ch]
            else:
                node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isWord:
                    return True
            elif w[0] == '.':
                for child in node.children.values():
                    stack.append((child, w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n, w[1:]))
        return False

    def basic_search(self, word):
        node  = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node and node.isWord



if __name__ == "__main__":
    root = WordDictionary()
    root.addWord("MAN")
    root.addWord("BAN")
    root.addWord("MAT")
    root.addWord("BAT")
    print(root.search("B.N"))
    print(root.basic_search("MANA"))