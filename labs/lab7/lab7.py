"""
Name: Aidan Mast
lab6.py

Problem: Write program that take in a file as input and outputs names, weighted averages, and total average.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    data = (open(in_file_name).read().rstrip().split("\n"))
    people = len(data)
    class_total = 0
    real_people = 0
    out_lines = []
    for index in range(people):
        person_data = data[index].split(":")
        grades_and_weights = person_data[1].lstrip().split(" ")
        tests = int(len(grades_and_weights) / 2)
        final_grade = 0
        weight_total = 0
        for value in range(tests):
            weighted_test = (eval(grades_and_weights[value * 2]) * (eval(grades_and_weights[value * 2 + 1]))) / 100
            final_grade = final_grade + weighted_test
            weight_total = weight_total + eval(grades_and_weights[value * 2])
        if weight_total == 100:
            out_lines.append(person_data[0] + "\'s average: " + str(round(final_grade, 1)))
            class_total = class_total + final_grade
            real_people = real_people + 1
        elif weight_total > 100:
            out_lines.append(person_data[0] + "\'s average: Error: The weights are more than 100.")
        else:
            out_lines.append(person_data[0] + "\'s average: Error: The weights are less than 100.")
    if real_people > 0:
        class_average = class_total / real_people
        out_lines.append("Class average: " + str(round(class_average, 1)))
    output_message = "\n".join(out_lines)
    avg_file = open("avg.txt", "w")
    avg_file.write(output_message)


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
