def maxProduct(nums) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
nums = [1,4,2,3,6,3]
#listni o'zini ekranga chiqaradi
print(nums)
print(maxProduct(nums))
