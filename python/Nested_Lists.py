# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())

nested_list = []
score_set = set()
for i in range(1,2*n+1,2):
    student_name = input().strip()
    student_score = float(input().strip())
    nested_list.append((student_name, student_score))
    score_set.add(student_score)

score_set = sorted(score_set)
if len(score_set) < 2:
        print("Not enough unique scores to determine the second lowest.")
else:
    second_lowest_score = score_set[1]
    student_list = []
    for item in nested_list:
        if item[1] == second_lowest_score:
            student_list.append(item[0])
        
for name in sorted(student_list):
     print(name)
