class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lookup = {}

        for letter in s:
            lookup[letter] = lookup.get(letter, 0) + 1

        for letter in t:
            if letter not in lookup or lookup[letter] == 0:
                return False
            lookup[letter] -= 1

        return True


solution = Solution()

print(solution.isAnagram("ccbc", "bbcc"))
