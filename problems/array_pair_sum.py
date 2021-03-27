def array_pair_sum(self, nums: List[int]) -> int:
    nums.sort()

    sum = 0
    for i in range(int(len(nums)/2)):
        sum += nums[2 * i]

    return sum
