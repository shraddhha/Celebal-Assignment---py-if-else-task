if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}
    
    for _ in range(n):
        line = input().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores
    
    query_name = input()
    
    # Calculate average
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    
    # Print average with 2 decimal places
    print(f"{average:.2f}")
