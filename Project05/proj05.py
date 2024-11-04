#######################################################################################################################
#
# Computer Project 05
# the below python script helps us to manage scores of students
# it uses basic files and exceptions and list and tuples
# Each subject includes various components to provide a
# comprehensive evaluation of the student's abilities in that area.
# 1: The maximum grade a student received in a single subject
# 2: The average subject grade a student received
# 3: Individual information
# 4: The average grade of a subject over all students
# 5: The number of students with an average grade exceeding given threshold X
# 6: The name of student having the highest average grade
# 7: The name of student having the highest grade of given subject name
# Enter any other key(s) to exit
#
#######################################################################################################################

import csv  # you don't have to use it
from operator import itemgetter


# subject_lst = ["English", "Math", "Science"] # List of valid subjects


def get_file_input(prompt):
    """
    here the file in inputted
    :param prompt:
    :return:
    """
    while True:
        file_name = input(prompt)
        try:
            x = open(file_name)
            return x, file_name
        except FileNotFoundError:
            print("Error. File does not exist")


def max_grade(names_file, student_name):
    """

    :param names_file:
    :param student_name:
    :return:
    """
    file = open(names_file, 'r')
    new_list = []
    for line in file:
        new_list.append(line.strip())
    while True:
        student_name = input(":~Enter a person name ~:")
        if student_name in new_list:
            index_name = new_list.index(student_name)
            print("--------------")
            return index_name
        else:
            print("Invalid name or does not exist")

    file.close()


def sum_english_file(english_file, index_name):
    """

    :param english_file:
    :param index_name:
    :return:
    """
    file = open(english_file, 'r')
    for i, line in enumerate(file):
        if i == index_name:
            my_list = []
            for num in line.split(','):
                if num != '':
                    my_list.append(int(num))
            sum_english = sum(my_list)
            return sum_english, my_list


def average(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    total = int(a) + int(b) + int(c)
    avg = total / 3
    print(f"Average grade score: {avg:.1f}")
    return avg


def individual_score(a, b, c, d, e, f):
    """

    :param a:
    :param b:
    :param c:
    :param d:
    :param e:
    :param f:
    :return:
    """

    print(f"English: {a}\nSpeaking: {d[0]} Writing: {d[1]} Reading: {d[2]} Listening: {d[3]}")
    print("--------------")
    print(f"Math: {c}\nGeometry: {f[0]} Arithmetic: {f[1]} Logic: {f[2]}")
    print("--------------")
    print(f"Science: {b}\nBiology: {e[0]} Chemistry: {e[1]} Physics: {e[2]}")


def subject_average(name_file, math_file, science_file, english_file):
    """

    :param name_file:
    :param math_file:
    :param science_file:
    :param english_file:
    :return:
    """
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    while True:
        user = input(":~Enter a subject name ~:")
        if user == "Math" or user == "English" or user == "Science":
            if user == "Math":
                name_file = math_file
            elif user == "Science":
                name_file = science_file
            elif user == "English":
                name_file = english_file
            file = open(name_file, "r")
            emp = []
            for line in file:
                line = line.strip()
                line = line.split(",")
                total = 0
                for num in line:
                    if num != '':
                        num = int(num)
                        total += num
                emp.append(total)
            avg_one = sum(emp) / len(emp)
            print("--------------")
            print(f"Average grade score: {avg_one:.1f}")
            return avg_one
        else:
            print("Invalid name or does not exist")


def idk(name_file, math_file, science_file, english_file):
    """

    :param name_file:
    :param math_file:
    :param science_file:
    :param english_file:
    :return:
    """
    while True:
        user = input(":~Enter a subject name ~:")
        if user == "Math" or user == "English" or user == "Science":
            if user == "Math":
                name_file = math_file
            elif user == "Science":
                name_file = science_file
            elif user == "English":
                name_file = english_file
            break
        else:
            print("Invalid name or does not exist")
            continue
    file = open(name_file, "r")
    return file


def student_max_grade_avg(name_file, math_file, science_file, english_file):
    """

    :param name_file:
    :param math_file:
    :param science_file:
    :param english_file:
    :return:
    """
    names = []

    math_grades = []

    science_grades = []

    english_grades = []
    file = open(name_file, "r")
    for line in file:
        names.append(line.strip())
    open_one = open(math_file, "r")
    for line in open_one:
        math_grades.append(line.strip())
    open_two = open(science_file, "r")
    for line in open_two:
        science_grades.append(line.strip())
    open_three = open(english_file, "r")
    for line in open_three:
        english_grades.append(line.strip())
    tot_list = []
    eng_scores = []
    mth_scores = []
    sci_scores = []
    for i in range(len(names)):
        mth = ""
        sci = ""
        eng = ""
        name = names[i].strip()
        mth = math_grades[i].strip().split(",")
        sci = science_grades[i].strip().split(",")
        en = english_grades[i].strip().split(",")
        total = 0
        for grade in mth:
            if grade:
                numeric_grade = int(grade)
                total += numeric_grade
        mth_scores.append(total)
        for grade in sci:
            if grade:
                numeric_grade = int(grade)
                total += numeric_grade
        sci_scores.append(total)
        for grade in en:
            if grade:
                numeric_grade = int(grade)
                total += numeric_grade
        eng_scores.append(total)
        tot_list.append((name, total))

    max_total = -1
    max_name = ""
    for name, total in tot_list:
        if total > max_total:
            max_total = total
            max_name = name
        if total == max_total:
            new_name = name
            index_one = names.index(name)
            index_two = names.index(max_name)
            if eng_scores[index_one] < eng_scores[index_two]:
                max_name = new_name
            elif mth_scores[index_one] < mth_scores[index_two]:
                max_name = new_name
            elif sci_scores[index_one] < sci_scores[index_two]:
                max_name = new_name
            else:
                max_name = name

    max_avg = max_total / 3
    print("--------------")
    print(f"Name: {max_name}")
    print(f"Average grade score: {max_avg:.1f}")


def student_subject_max(name_file, math_file, science_file, english_file):
    """

    :param name_file:
    :param math_file:
    :param science_file:
    :param english_file:
    :return:
    """
    print("\n   Available subjects:\n                            Math, Science, and English \n")
    file = idk(name_file, math_file, science_file, english_file)
    name_file = open(name_file, "r")
    names = []
    num_list = []
    name_list = []
    for line in file:
        names.append(line.strip())
        total = 0
        line = line.strip()
        line = line.split(",")
        for num in line:
            if num != '':
                num = int(num)
                total += num
        num_list.append(total)
    for name in name_file:
        name_list.append(name)
    max_num = 0
    student = ""

    for i, num in enumerate(num_list):
        if i > len(num_list) - 1:
            break
        if num > max_num:
            max_num = num
            student = name_list[i].strip()
            y = i
        elif num == max_num:
            new_student = name_list[i]
            score_one = names[y]
            score_two = names[i]
            for x in range(0, len(score_one)):
                if score_one[x] < score_two[x]:
                    student = new_student
                elif y > i:
                    student = new_student.strip()
                else:
                    student = student.strip()

    print("--------------")
    print(f"Name: {student}")
    print(f"Grade score: {max_num}")


def threshold(name_file, math_file, science_file, english_file):
    """

    :param name_file:
    :param math_file:
    :param science_file:
    :param english_file:
    :return:
    """
    while True:
        user = int(input(":~Enter a grade threshold ~:"))
        if user < 0:
            print("Invalid grade score")
            continue
        if user > 100:
            print("Invalid grade score")
            continue
        else:
            names = []

            math_grades = []

            science_grades = []

            english_grades = []
            file = open(name_file, "r")
            for line in file:
                names.append(line.strip())
            open_one = open(math_file, "r")
            for line in open_one:
                math_grades.append(line.strip())
            open_two = open(science_file, "r")
            for line in open_two:
                science_grades.append(line.strip())
            open_three = open(english_file, "r")
            for line in open_three:
                english_grades.append(line.strip())
            tot_list = []
            eng_scores = []
            mth_scores = []
            sci_scores = []
            for i in range(len(names)):
                mth = ""
                sci = ""
                eng = ""
                name = names[i].strip()
                mth = math_grades[i].strip().split(",")
                sci = science_grades[i].strip().split(",")
                en = english_grades[i].strip().split(",")
                total = 0
                for grade in mth:
                    if grade:
                        numeric_grade = int(grade)
                        total += numeric_grade
                for grade in sci:
                    if grade:
                        numeric_grade = int(grade)
                        total += numeric_grade
                for grade in en:
                    if grade:
                        numeric_grade = int(grade)
                        total += numeric_grade
                avgg = total / 3
                tot_list.append(avgg)
            thres = []
            for x, y in enumerate(tot_list):
                if y > user:
                    thres.append(y)
            length = len(thres)
            print("--------------")
            print(f"The number of students having average grade score higher than {user} is: {length}")
            return user


def main():
    """

    :return:
    """
    student_name = ""

    x, name_file = get_file_input(":~Enter a student names file ~:")
    x, english_file = get_file_input(":~Enter a English grade score file ~:")
    x, math_file = get_file_input(":~Enter a Math grade score file ~:")
    x, science_file = get_file_input(":~Enter a Science grade score file ~:")

    menu = '''
        Menu : 
            1: The maximum grade a student received in a single subject
            2: The average subject grade a student received
            3: Individual information
            4: The average grade of a subject over all students
            5: The number of students with an average grade exceeding given threshold X
            6: The name of student having the highest average grade
            7: The name of student having the highest grade of given subject name
                Enter any other key(s) to exit
    '''
    while True:
        print(menu)
        user_input = input(":~Input a choice ~:")
        if user_input == "1":
            subjects = ""
            index_name = max_grade(name_file, student_name)
            sum_english, x = sum_english_file(english_file, index_name)
            sum_science, y = sum_english_file(science_file, index_name)
            sum_math, z = sum_english_file(math_file, index_name)
            ne_list = [sum_english, sum_science, sum_math]
            max_score = max(ne_list)
            print(f"Highest grade score: {max_score}")
            if max_score == sum_english:
                subjects += "English"
            if max_score == sum_science:
                subjects += " " + "Science"
            if max_score == sum_math:
                subjects += " " + "Math"
            print(f"Subject name: {subjects}")
        elif user_input == "2":
            index_name = max_grade(name_file, student_name)
            sum_english, english_list = sum_english_file(english_file, index_name)
            sum_science, science_list = sum_english_file(science_file, index_name)
            sum_math, math_list = sum_english_file(math_file, index_name)
            avg = average(sum_english, sum_science, sum_math)
        elif user_input == "3":
            index_name = max_grade(name_file, student_name)
            sum_english, english_list = sum_english_file(english_file, index_name)
            sum_science, science_list = sum_english_file(science_file, index_name)
            sum_math, math_list = sum_english_file(math_file, index_name)
            individual_score(sum_english, sum_science, sum_math, english_list, science_list, math_list)
        elif user_input == "4":
            subject_average(name_file, math_file, science_file, english_file)
        elif user_input == "5":
            threshold(name_file, math_file, science_file, english_file)
        elif user_input == "6":
            student_max_grade_avg(name_file, math_file, science_file, english_file)
        elif user_input == "7":
            student_subject_max(name_file, math_file, science_file, english_file)
        else:
            print("Thank you")
            exit()


# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in a function.
if __name__ == "__main__":
    main()
