################################
# Yonten Kinley Tenzin 
# SWE 
# 02230313
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Solution Score
# Task 1: 6474 
# Task 2: 2519 
################################

# Read the input file
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(', ') for line in lines]

# Check if two assignments overlap
def assignments_overlap(assignment1, assignment2):
    (start1, end1), (start2, end2) = map(convert_to_range, (assignment1, assignment2))
    return start1 <= end2 and start2 <= end1

# Convert assignment string to a tuple of start and end
def convert_to_range(assignment):
    (start, end) = map(int, assignment.split('-'))
    return (start, end)

# Check if two assignments fully overlap
def assignments_fully_overlap(assignment1, assignment2):
    (start1, end1), (start2, end2) = map(convert_to_range, (assignment1, assignment2))
    return start1 <= start2 and end2 <= end1

# Task 1: Calculate the total number of people and overlapping assignments
def task_1(assignments):
    num_people = 0
    num_overlapping = 0
    for assignment in assignments:
        num_people += 2
        if assignments_overlap(assignment[0], assignment[1]):
            num_overlapping += 1
    return (num_people, num_overlapping)

# Task 2: Calculate the total number of assignments that fully overlap
def task_2(assignments):
    num_fully_overlapping = 0
    for assignment in assignments:
        if assignments_fully_overlap(assignment[0], assignment[1]):
            num_fully_overlapping += 1
    return num_fully_overlapping

# Main function
def main():
    # Read the input file
    filename = "input_3_cap2.txt"
    assignments = read_input(filename)

    # Solve Task 1
    num_people, num_overlapping = task_1(assignments)
    print(f"There were {num_people} people assigned and there are {num_overlapping} overlapping space assignments")

    # Solve Task 2
    num_fully_overlapping = task_2(assignments)
    print(f"There were {num_fully_overlapping} assignments that overlap completely")

# Run the main function
if __name__ == "__main__":
    main()