def two_sum(self, nums: List[int], target: int) -> List[int]:

    answer = []
    for i, num in enumerate(nums):
        t = 1
        while i + t < len(nums):
            if nums[i] + nums[i+t] == target:
                answer = [i, i+t]
                break
            t += 1

        if answer:
            break

    return answer
