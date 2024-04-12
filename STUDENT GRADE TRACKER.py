from tabulate import tabulate

# Function to get student information
def get_student_info():
    student_name = input("Enter the student's name: ")
    student_age = input("Enter the student's age: ")
    school_name = input("Enter the school name: ")
    standard = input("Enter the student's standard: ")
    return student_name, student_age, school_name, standard

# Function to get grades for each subject
def get_grades():
    grades = []
    number_of_subjects = int(input("Enter the number of subjects: "))

    for _ in range(number_of_subjects):
        subject = input("Enter the subject name: ")
        grade = float(input(f"Enter the grade for {subject} (out of 10): "))
        grades.append([subject, grade])

    return grades

# Function to calculate the average grade
def calculate_average(grades):
    total = sum(grade for _, grade in grades)
    number_of_grades = len(grades)
    average = total / number_of_grades
    return average

# Function to calculate the percentage
def calculate_percentage(average):
    return average * 10

# Main function to orchestrate the program flow
def main():
    try:
        student_name, student_age, school_name, standard = get_student_info()
        student_grades = get_grades()
        average_grade = calculate_average(student_grades)
        percentage = calculate_percentage(average_grade)
        cgpa = average_grade  # Assuming CGPA is the same as the average grade out of 10
        sgpa = average_grade  # Assuming SGPA is the same as the average grade for the semester

        # Student information and grades for display
        student_info = [
            ["Student Name", student_name],
            ["Age", student_age],
            ["School", school_name],
            ["Standard", standard],
            ["Average", average_grade],
            ["Percentage", f"{percentage}%"],
            ["CGPA", cgpa],
            ["SGPA", sgpa]
        ]

        # Displaying the student information and grades in a tabular format
        print("\nStudent Information and Grades:")
        print(tabulate(student_info, headers=["Category", "Detail"], tablefmt="fancy_grid"))
        print("\nSubject Grades:")
        print(tabulate(student_grades, headers=["Subject", "Grade"], tablefmt="fancy_grid"))

    except ValueError as e:
        print(f"An error occurred: {e}. Please enter valid numeric values for age and grades.")

# Entry point of the program
if __name__ == "__main__":
    main()
