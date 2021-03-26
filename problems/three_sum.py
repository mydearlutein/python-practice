def three_sum(self, nums: List[int]) -> List[List[int]]:
    answer = []

    # 순서를 정렬해 편의성 도모
    nums.sort()

    #기준이 되는 값을 마지막 바로 전 값까지로 정의
    for i in range(len(nums) -2):
        # 기준이 되는 값이 같으면 중복되므로 스킵
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 기준이 되는 값의 바로 다음 원소를 left, 리스트 마지막 값을 right로 설정
        left, right = i + 1, len(nums) - 1

        # left, right가 같은 위치가 되지 않을 때까지 반복
        while left < right:
            # 3 숫자의 합 계산
            sum = nums[i] + nums[left] + nums[right]

            # 합이 0보다 작으면 작은 숫자를 다음 큰 숫자로 변경
            if sum < 0:
                left += 1
            # 합이 0보다 크면 큰 숫자를 다음 작은 숫자로 변경
            elif sum > 0:
                right -= 1
            else:
                # 합이 0이면 결과값에 저장
                answer.append([nums[i], nums[left], nums[right]])

                # 다음 이동시킬 값이 직전 원소와 같으면 중복되므로 패스
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 중복되지 않는 다음 원소로 이동
                left += 1
                right -= 1

    return answer
