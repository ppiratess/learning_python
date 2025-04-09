from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(str)

        return list(result.values())


solution = Solution()

print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
