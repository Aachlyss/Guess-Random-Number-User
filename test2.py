def distinct(nums):
    nums_list = []
    for num in nums:
        int_num = int(num)
        if nums_list.__contains__(int_num):
            continue
        else:
            nums_list.append(int_num)
    print(nums_list)

nums = [1, 1, 2]

distinct(nums)
