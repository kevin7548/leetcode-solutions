class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

        return [start + 1, end + 1]

    # if one solution 보장 X
        # while start < end:
        #     total = numbers[start] + numbers[end]
        #     if total == target:
        #         return [start + 1, end + 1]
        #     elif total > target:
        #         end -= 1
        #     else:
        #         start += 1
