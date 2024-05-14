def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Enter Your Name")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("Enter your Math Score")
    science_score = input("Enter your Science Score")
    english_score = input("Enter your English Score")

    # Calculate the average grade
    average_grade = (int(math_score) + int(science_score) + int(english_score)) // 3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"The student named {student_name} Average Grade is {average_grade}.")