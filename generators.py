def square_nums(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_nums([1,2,3,4,5])

# print(my_nums)

def square_numbers(nums):
    for i in nums:
        yield (i * i)

my_nums_1 = square_numbers([1,2,3,4,5])
# print(next(my_nums_1))

for num in my_nums_1:
    print(num)

my_nums = (x * x for x in [1,2,3,4,5])
print(my_nums)
for num in my_nums:
    print(num)

print(list(my_nums))
