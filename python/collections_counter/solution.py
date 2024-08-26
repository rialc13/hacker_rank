# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
shoeStock = int(input())
shoeStockList = list(int(size) for size in input().split())
customers = int(input())

# shoeStock = 10
# shoeStockList = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
# customers = 6
if len(shoeStockList) != shoeStock:
    print(f"Error: Expected {shoeStock} shoe sizes, but got {len(shoeStockList)}.")
else:
    shoeListCounter = Counter(shoeStockList)
    # print(shoeListCounter)

customersData = []
for _ in range(customers):
    size, price = map(int, input().split())
    customersData.append((size, price))

# print(customersData)

earnings = 0
for size, price in customersData:
    if shoeListCounter[size] > 0:
        earnings += price
        shoeListCounter[size] -= 1
    else:
        earnings

print(earnings)
# # Checking count of specific element
# print(shoeListCounter[5])
# # Decrease count of a specific element
# if shoeListCounter[5] > 0:
#     shoeListCounter[5] -= 1
# # Check & delete if key count reaches 0
# if shoeListCounter[5] == 0:
#     del shoeListCounter[5]
