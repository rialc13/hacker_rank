# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n,m = map(int, input().split())
# list_A = []
# for index in range(1,n+1):
#     letter = input().strip()
#     list_A.append((letter,index))
list_A = [(input().strip(),index) for index in range(1,n+1)]
d = defaultdict(list)

# for letter, index in list_A:
#     d[letter].append(index)
list_A = [d[letter].append(index) for letter, index in list_A]
# print(type(d.keys()))

# list_B = []
# for index in range(n+2,n+2+m):
#     letter = input().strip()
#     list_B.append(letter)
list_B = [(input().strip()) for index in range(n+2,n+2+m)]

# for item in list_B:
#     output_list = d.get(item)
#     if output_list == None:
#         print(-1)
#     else:
#         print(*d.get(item), sep=' ')

output_list = [print(-1) if d.get(item) is None else print(*d.get(item), sep=' ') for item in list_B]
# print(output_list)