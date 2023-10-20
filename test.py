class Solution(object):
    def removeDuplicates(nums):
        nums_list = []
        nums.sort()
        for num in nums:
            if nums_list.__contains__(num):
                continue
            else:
                nums_list.append(num)
        nums_list.sort()
        nums_count = len(nums_list)
        print(nums_count)

    nums = [0,0,1,1,1,2,2,3,3,4]

    removeDuplicates(nums)
