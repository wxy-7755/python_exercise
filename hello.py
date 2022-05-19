# 1Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# r = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         r.append(i)
# print(len(r))
# print(r)

# #solution
# l = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
# print(len(l))
# print(','.join(l))

# 2Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# a = int(input("请输入一个数字："))
# cj = 1
# while a > 0:
#     cj *= a
#     a -= 1
# print(cj)

# solution
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# x = int(input("请输入一个数字："))
# print(fact(x))

# 3Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# #solution
# b = dict()
# a = int(input("请输入一个数字："))
# for i in range(1,a+1):
#     b[i] = i*i
# print(b)

# 4Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# a = list()
# n = int(input("你需要输入几位数字"))
#
# while n > 0 :
#     #输入的数字
#     x = int(input("请输入%d位" % n))
#     a.append(x)
#     n -= 1
# print(a)
# print(tuple(a))

#solution
# values = input()
# l = values.split(",")
# t = tuple(l)
# print(l)
# print(t)

