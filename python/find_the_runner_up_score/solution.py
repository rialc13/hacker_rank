# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
new_arr = []
for element in arr:
    if element not in new_arr:
        new_arr.append(element)

new_arr = sorted(new_arr,reverse=True)
print(new_arr[1])