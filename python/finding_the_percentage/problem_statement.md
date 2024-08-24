# Problem

You are given a dictionary containing key/value pairs of `name:[marks]` for a list of students. The task is to calculate the average of the marks for a given student name and print it, formatted to 2 decimal places.

## Example

marks key:value pairs are
'alpha': [20,30,40]
'beta': [30,50,70]
query_name = 'beta'

The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.00.

## Input Format

- The first line contains an integer `n`, the number of students' records.
- The next `n` lines contain the names of the students and their respective marks, separated by spaces.
- The last line contains `query_name`, the name of the student whose average marks you need to calculate.

## Constraints

- `2 <= n <= 10`
- `0 <= marks <= 100`

## Output Format

Print one line: the average of the marks obtained by the specified student, correct to 2 decimal places.

## Sample Input

> 3
>
> Krishna 67 68 69
>
> Arjun 70 98 63
>
> Malika 52 56 60
>
> Malika

## Sample Output

> 56.00


## Explanation

Marks for Malika are `[52, 56, 60]`, whose average is `56.00`.