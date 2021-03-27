def product_except_self(self, nums: List[int]) -> List[int]:
    out = []
    product = 1

    # 자신을 제외한 왼쪽의 곱 리스트
    for i in range(0, len(nums)):
        out.append(product)
        product = product * nums[i]

    # 왼쪽의 곱에 오른쪽 끝부터 순서대로 값들을 곱해나감
    product = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * product
        product = product * nums[i]

    return out
