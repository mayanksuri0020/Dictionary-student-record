# Function to create a student dictionary
def create_student(stdid, stdname, standard, age, hindi, english, maths, science, computer):
    total = hindi + english + maths + science + computer
    student = {
        'stdid': stdid,
        'stdname': stdname,
        'standard': standard,
        'age': age,
        'hindi': hindi,
        'english': english,
        'maths': maths,
        'science': science,
        'computer': computer,
        'total': total
    }
    return student

# Function to print the student dictionary in tabular format
def print_students_table(students):
    # Print the table header
    print(f"{'StdID':<10}{'Name':<20}{'Standard':<10}{'Age':<5}{'Hindi':<10}{'English':<10}{'Maths':<10}{'Science':<10}{'Computer':<10}{'Total':<10}")
    print('-' * 95)
    
    # Print each student's details
    for student in students:
        print(f"{student['stdid']:<10}{student['stdname']:<20}{student['standard']:<10}{student['age']:<10}{student['hindi']:<10}{student['english']:<10}{student['maths']:<10}{student['science']:<10}{student['computer']:<10}{student['total']:<10}")

# Example usage
student1 = create_student('STD01','Ashish'    ,     '10th'  ,   15      ,88  ,86,92,97,65)
student2 = create_student('STD02','Abhi'      ,     '10th'  ,   16      ,70  ,82,88,59,89)
student3 = create_student('STD03','Aman'      ,     '10th'  ,   15      ,60  ,91,94,81,92)
student4 = create_student('STD04','kratika'   ,     '10th'  ,   15      ,76  ,86,90,90,78)
student5 = create_student('STD05','mona'      ,     '10th'  ,   15      ,59  ,75,39,82,65)
student6 = create_student('STD06','pratush'   ,     '10th'  ,   16      ,91  ,69,58,84,91)
student7 = create_student('STD07','ragini'    ,     '10th'  ,   15      ,51  ,91,91,72,98)
student8 = create_student('STD08','kartik'    ,     '10th'  ,   15      ,70  ,68,70,68,67)
student9 = create_student('STD09','Anshika'   ,     '10th'  ,   15      ,81  ,81,50,90,55)
student10 = create_student('STD10','Aira'     ,     '10th'  ,   15      ,84  ,80,50,80,58)

# List of students
students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]

# Print the students table
print_students_table(students)

# Function to print names of students with English marks greater than 50
def print_students_with_english_above_50(students):
    print("Students with English marks greater than 50:")
    for student in students:
        if student['english'] > 50:
            print(f"{student['stdname']}")

print()
print_students_with_english_above_50(students)

# Function to find and print the top four scorers in Maths using only dictionaries
def print_top_four_scorers_in_maths(students):
    # Extract student names and their Maths marks into a list of tuples
    maths_scores = [(student['stdname'], student['maths']) for student in students]
    
    # Sort the list of tuples by Maths marks in descending order
    sorted_maths_scores = sorted(maths_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top four scorers
    top_four = sorted_maths_scores[:4]
    
    # Print the top four scorers
    print("\nTop Four Scorers in Maths:")
    for name, maths in top_four:
        print(f"{name} - Maths: {maths}")
# Print top four scorers in Maths
print_top_four_scorers_in_maths(students)


# Function to find and print the bottom three scorers in Computer using only dictionaries
def print_bottom_three_scorers_in_computer(students):
    # Extract student names and their Computer marks into a list of tuples
    computer_scores = [(student['stdname'], student['computer']) for student in students]
    
    # Sort the list of tuples by Computer marks in ascending order
    sorted_computer_scores = sorted(computer_scores, key=lambda x: x[1])
    
    # Get the bottom three scorers
    bottom_three = sorted_computer_scores[:3]
    
    # Print the bottom three scorers
    print("\nBottom Three Scorers in Computer:")
    for name, computer in bottom_three:
        print(f"{name} - Computer: {computer}")

# Print bottom three scorers in Computer
print_bottom_three_scorers_in_computer(students)
