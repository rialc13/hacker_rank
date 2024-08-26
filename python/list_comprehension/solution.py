# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

########################### EXAMPLE 1 #################################
# ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
# ListOfThreeMultiples = []
# for x in range(10):
#     if x % 3 == 0:
#         ListOfThreeMultiples.append(x)

# print(ListOfThreeMultiples)

########################### EXAMPLE 2 #################################
# results = []
# x = 1
# y = 1
# z = 2
# n = 3
# for a in range(x+1):
#     for b in range(y+1):
#         for c in range(z+1):
#             if a+b+c != n:
#                 results.append([a, b, c])

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

results = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(results)