age = 18

if age >= 18:
    print("you can vote.")
else:
    print("you can not vote yet.")


temperature = 28

if temperature > 30:
    print("its a hot day")
elif 20 <= temperature <= 30:
    print("The weather is pleasent")
else:
    print("its a cold day")


student_gpa =   4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a  partial scolarship ")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is eligible for a  full scolarship ")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scolarship ")
else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a  scolarship ")