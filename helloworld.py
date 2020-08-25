

# ss = s.split(';')

# sss = [ss.split('|') for ss in s.split(';')]
# list1 = list(map(lambda ss:ss.split('|') ,s.split(';')))

# print(list1)


# def my_split(s,seqs):
#     res = [s]
#     for seq in seqs:
#         t = []
#         list(map(lambda ss:t.extend(ss.split(seq)),res))
#         res = t
#     return res
#
# print(my_split(name,';|\t,'))
#
# name = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# import re
# print(re.split('[;,|\t]',name))

#用来测试一下

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # res = list(zip(*a))
# # res2 = map(list, zip(*a))[::-1]
# # res3 = map(list, zip(*a[::-1]))
# res2 = list(zip(*a[::-1]))  # 顺时针旋转90
# res3 = list(zip(*a))[::-1]  # 逆时针旋转90
# # print(res)
# print(res2)
# print(res3)
#
# import heapq
#
# arr = [1, 3, 5, 6, 2, 65, 22, 33]
# heapq.heapify(arr)
# a = heapq.nlargest(3, arr)
# print(arr)
# print(a)
#
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(arr)
# heapq.heappush(arr, 19)
# print(arr)
# # print(arr[0])
# import random
#
# letters = 'abcdefghijklmnopqrstuvwxyz'
# # letter_dict = {k: v for k in letters}
# dic = {'a':2, 'b':3}
# # print(dic[2])
# class Solution:
#     def search(self, nums: [int], target: int) -> int:
#         def helper(tar):
#             i, j = 0, len(nums) - 1
#             while i <= j:
#                 m = (i + j) // 2
#                 if nums[m] <= tar:
#                     i = m + 1
#                 else:
#                     j = m - 1
#             return i
#
#         return helper(target) - helper(target - 1)
#
#
# if __name__ == '__main__':
#     test = Solution()
#     a = test.search([1, 7, 7, 8, 8, 10], 10)
#     print(a)





# res = []
# s = 'I am a   student'
# for k in range(len(s)):
#     if s[k] != ' ':
#        tmp = k
#        k += 1
#
#     else:
#         a = [s[i] for i in range(tmp, k)]
#         res.append(a)
# print(res)
# print(nums)
# print(''.join(nums))


s = '  I da d   ffff '
print(str.strip(s))
