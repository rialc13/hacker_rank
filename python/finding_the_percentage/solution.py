# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def calculate_average(student_marks, query_name):
    if query_name not in student_marks.keys():
        return f"No records found for {query_name}."
    else:
        total_marks = sum(student_marks[query_name])
        subjects = len(student_marks[query_name])
        if subjects == 0:
            return "No subject marks found for this student"
        else:
            average_marks = (total_marks/subjects)
            return f"{average_marks:.2f}"
        
# Example usage:
result = calculate_average(student_marks, query_name)
print(result)