from typing import List


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    map_ = {}
    left = 0
    result = 0

    for i in range(len(s)):
        if s[i] in map_:
            map_[s[i]] += 1
        else:
            map_[s[i]] = 1

        while len(map_) > k:
            if map_[s[left]] > 1:
                map_[s[left]] -= 1
            else:
                del map_[s[left]]
            left += 1

        result = max(sum(map_.values()), result)

    return result


# print(lengthOfLongestSubstringKDistinct("eceba", 2))


def totalFruit(tree: List[int]) -> int:
    map_ = {}
    result = 0
    left = 0

    for i in range(len(tree)):
        if tree[i] in map_:
            tree[i] += 1
        else:
            tree[i] = 1

        while len(map_) > 2:
            if map_[tree[left]] > 1:
                map_[tree[left]] -= 1
            else:
                del map_[tree[left]]
            left += 1

        result = max(result, sum(map_.values()))

    return result

print(totalFruit([1,2,1]))