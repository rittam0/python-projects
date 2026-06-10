nums= [10,20,30,40]
sorted_nums= sorted(nums)
has_duplicate=False
for i in range(len(sorted_nums)):
    if sorted_nums[i]==sorted_nums[i+1]:
        has_duplicate=True
        break
print(f"does array contain duplicate: {has_duplicate}")