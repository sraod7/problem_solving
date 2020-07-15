class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        stack = [(node, word)]

        while stack:
            n, w = stack.pop()

            if w == '' and n.is_word:
                return True

            if w == '':
                continue

            next_char = w[0]

            if next_char == '.':
                for key, val in n.children.items():
                    stack.append((val, w[1:]))
            else:
                if next_char in n.children:
                    stack.append((n.children[next_char], w[1:]))

        return False

obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')

print(obj.search('pad'))
print(obj.search('bad'))
print(obj.search('.ad'))
print(obj.search('b..'))
