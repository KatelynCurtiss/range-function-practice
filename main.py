# Katelyn Curtiss
# November 1 2024
# Range Function Practice


# 4-3. Counting to twenty
# numbers = list(range(1 , 21))
# for n in numbers:
#   print(n)


# 4-4. One million
# onemillion = range(1 , 1000000001)
# for n in onemillion:
#     print(n)


# for number in range(1,1001):
#    print(number)

# # 4-5. Summing a million
# million = range(1 , 1000000000)
# minimum = min(million)
# print(f'The smallest number was: {minimum}')
# max(million)
# sum(million)
# for i in million:
#     print(i)


# # 4-6. Odd numbers 
# odd_numbers = range(1, 12, 1)
# for x in odd_numbers:
#    if x % 2 == 1:
#     print(x)

# # 4-7. Threes
# multiple_threes = range(3,31, 3)
# for x in multiple_threes:
#    print(x)


# # 4-8. Cubes
# cubes = [value**3 for value in range(1,10) ]
# print(cubes)
   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes = []

for number in numbers:
   result = number ** 3
   cubes.append(result)
print(numbers)
print(cubes)



