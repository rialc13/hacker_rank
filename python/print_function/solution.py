# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())

def create_list(number):
    num_1 = 1
    if number == num_1:
        return number
    else:
        x = []
        while num_1 < number+1:
            x.append(num_1)
            num_1 += 1
    return(x)

array = create_list(n)
print(*array, sep='', end='\n')