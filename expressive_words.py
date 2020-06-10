class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def group_chars(s):
            arr = [(char, len(list(group))) for char, group in itertools.groupby(s)]

            return list(zip(*arr))

        s_group, s_counts = group_chars(S)
        result = 0

        for word in words:
            word_group, word_counts = group_chars(word)
            if word_group != s_group:
                continue

            result += all(
                s_count >= max(word_count, 3) or s_count == word_count for s_count, word_count in
                zip(s_counts, word_counts))

        return result