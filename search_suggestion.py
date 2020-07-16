from typing import List


class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    root = Trie()

    node = root
    for product in sorted(products):
        _insert(product, root)

    return _search(searchWord, root)


def _insert(product: str, root: Trie) -> None:
    trie = root
    for char in product:
        if char not in trie.sub:
            trie.sub[char] = Trie()
        trie = trie.sub[char]
        trie.suggestion.append(product)
        trie.suggestion.sort()
        if len(trie.suggestion) > 3:
            trie.suggestion.pop()


def _search(searchWord: str, root: Trie) -> List[List[str]]:
    ans = []
    for char in searchWord:
        if root:
            root = root.sub.get(char)
        ans.append(root.suggestion if root else [])
    return ans


class Node:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # initialize trie
        root = Node()

        # insert inputs products list

        for product in products:
            node = root
            for c in product:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                node.suggestions.append(product)
                node.suggestions.sort()

                if len(node.suggestions) > 3:
                    node.suggestions.pop()

        # search
        node = root
        res = []
        for c in searchWord:
            if node:
                node = node.children.get(c)
            res.append(node.suggestions if node else [])

        return res

obj = Solution()
print(obj.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                        "mouse"))

#
# print(suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"],
#                         "mouse"))
