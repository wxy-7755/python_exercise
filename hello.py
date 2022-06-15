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


### Question 5    5/23-1
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class TwoMethod(object):
#     def getString(self, name):
#         self.name = name
#         return name
#     def printString(self, name):
#         print(self.name)

#solution
# class TwoMethod(object):
#         def getString(self,name):
#             self.s = input()
#
#         def printString(self):
#             print(self.s.upper())
#
# strOBJ = TwoMethod()
# strOBJ.getString()
# strOBJ.printString()


# Question 6:   5/23-2
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# import math
#
# C, H = 50, 30
#
# str = input()
#
# D = str.split(',')
#
# for i in D:
#     Q = math.sqrt(int((2 * C * D)/int(H)),2)
#     print(Q)

#solution
# import math
#
# c, h = 50, 30
# value = []
#
# items = [x for x in input().split(',')]

# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))


# Question:   6/6-1
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]]

# Solution:
# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
#横取值
# rowNum=dimensions[0]
#列取值
# colNum=dimensions[1]
#在列表中插入列表
# 3 for i in range(3) => [3,3,3]

# my_list = [[0,0,0] for i in range(3)]
# print(my_list)

# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#[[0,0,0],[0,0,0],[0,0,0]]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
# print(multilist)
#总结思路：直接生成[[0,0,0],[0,0,0],[0,0,0]]二维数组，利用range()函数，重新遍历赋值


# Question: 6/9-1
# Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# input_str = input()
# word = input_str.split(',')
# word.sort()
# print(','.join(word))

#注意：sort()对原表进行列表排序，对原表直接操作，并不会返回一个新的列表，sort()方法需要单独使用

# Solution:
# ```python
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))


# Question£º  6/9-2
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


#补充：lower()大写字母转化成小写字母，swapcase()原大写变小写，小写变大写，title()首字母首字母转为大写，upper()小写
# upper()生成了新的字符串

# intems = input()
# intem = intems.upper()
# print(intem)

# Solution:
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)

# Question:   6/14-1
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# input_str = [x for x in input().split(' ')]
# my_list = []
# for i in range(len(input_str)):
#     if input_str[i] not in my_list:
#         my_list.append(input_str[i])
# my_list.sort()
# print(' '.join(my_list))

# Solution:
#学习 ：set()函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集
# 返回新的集合对象
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))



# Question:   6/14 -2
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# input_str = [int(x) for x in input().split(',')]
# my_list = []
# for i in input_str:
#     if i % 5 == 0:
#         my_list.append(i)
# print(my_list)

# 结果：
# 0100,0011,1010,1001
# [100, 1010]

# Solution:
#学习：int(x,base=10) int()函数用于将一个字符串或者数字转化为整形   x--字符串 base--进制数，默认十进制
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
# print(','.join(value))

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that
# each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

