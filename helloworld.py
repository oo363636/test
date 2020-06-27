

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

name = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
import re
print(re.split('[;,|\t]',name))
