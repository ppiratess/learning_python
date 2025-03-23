class Solution:
    def remove_duplicates(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        write_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        # returns unique number count
        # return write_index

        # returns unique list
        return nums[:write_index]


solution = Solution()
print(solution.remove_duplicates([1, 1, 1, 2, 3, 4, 4, 4]))
