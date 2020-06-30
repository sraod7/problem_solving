from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:

    # edge case check
    if not beginWord or not endWord or not wordList:
        return 0
    if endWord not in wordList:
        return 0

    # build out graph

    graph = {}

    for word in wordList:
        for i in range(len(beginWord)):
            search_word = word[:i] + '*' + word[i + 1:]
            if search_word in graph:
                graph[search_word].append(word)
            else:
                graph[search_word] = [word]

    # BFS to find the endword

    queue = [(beginWord, 1)]
    visited = {beginWord}

    while queue:
        word, level = queue.pop(0)

        for i in range(len(word)):
            search_word = word[:i] + '*' + word[i + 1:]
            if search_word in graph:
                for child_word in graph[search_word]:
                    if child_word == endWord:
                        return level + 1
                    if child_word not in visited:
                        visited.add(child_word)
                        queue.append((child_word, level + 1))

    return 0

