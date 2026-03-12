class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # O(N^2)까지 가능
        # 양 끝을 고정하고 Mid 순회가 아니라, left 고정 후 mid, right 좁히기
        nums.sort()
        triplet = []
        
        # left: i [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:    # nums 중복 skip
                continue
            
            left, right = i+1, len(nums)-1

            while left < right:
                sum_triplets = nums[i] + nums[left] + nums[right]
                
                if sum_triplets == 0:
                    triplet.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_triplets < 0:
                    left += 1
                else:
                    right -= 1
            
        return triplet

