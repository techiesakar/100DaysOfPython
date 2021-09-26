
# Method 1
# sum = 0
# for even in range(1, 101):
#     if even % 2 == 0:
#         sum = sum + even
# print(sum)

# Method 2
sum = 0
for even in range(2, 101, 2):
    sum += even
print(sum)
