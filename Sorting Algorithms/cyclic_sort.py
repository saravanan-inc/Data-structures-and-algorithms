nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

start = 0
end = len(nums)-1

while start <= end:
    if start != nums[start] and nums[start] <= end:
        temp = nums[nums[start]]
        nums[nums[start]] = nums[start]
        nums[start] = temp

    else:
        start += 1

print(nums)
