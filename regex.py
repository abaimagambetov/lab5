import re

# 1
# s = input()
# x = re.findall('ab*?', s)
#
# if x:
#     print(x)
# else:
#     print("not found!")


# 2
# s = input()
# x = re.findall("ab{2}|ab{3}", s)
#
# if x:
#     print(x)
# else:
#     print("not found!")


# 3
# s = input()
# x = re.findall("[a-z]+_[a-z]+", s)
#
# if x:
#     print(x)
# else:
#     print("not found!")


# 4
# s = input()
# x = re.findall("[A-Z][a-z]+", s)   # {1}
#
# if x:
#     print(x)
# else:
#     print("not found!")


# 5
# s = input()
# x = re.findall("a.*b", s)
#
# if x:
#     print(x)
# else:
#     print("not found!")


# 6
# s = input()
# x = re.sub("[ ,.]", ":", s)
# print(x)


# 7
# def fromsnaketocamel(s):
#     return ''.join(i.capitalize() or '_' for i in s)
#
#
# s = input().split('_')
# print(fromsnaketocamel(s))


# 8
# s = input()
# x = re.findall("[A-Z][^A-Z]*", s)
# print(x)


# 9
# s = input()
# x = re.findall("[A-Z][a-z]*", s)
# print(' '.join(x))


# 10
# def fromcameltosnake(s):
#     return '_'.join(re.sub('([A-Z][a-z]+)', r'\1', re.sub('([A-Z]+)', r'\1', s.replace(' - ', ' '))).split()).lower()
#
#
# s = input()
# print(fromcameltosnake(s))