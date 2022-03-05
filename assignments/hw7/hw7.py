"""
Name: Aidan Mast
hw7.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    message = open(in_file_name).read().replace("\n", " ").replace("\t", " ").rstrip().split(" ")
    out_lines = []
    for index in range(len(message)):
        value = str(index + 1) + " " + message[index]
        out_lines.append(value)
    out_message = "\n".join(out_lines)
    out_file_name = open(out_file_name, "w")
    print(out_message, file=out_file_name)


def hourly_wages(in_file_name, out_file_name):
    data = open(in_file_name).read().rstrip().split("\n")
    pay_log = []
    for index in range(len(data)):
        personal_data = data[index].split(" ")
        pay = (eval(personal_data[2]) + 1.65) * (eval(personal_data[3]))
        line = personal_data[0] + " " + personal_data[1] + " {:.2f}".format(pay)
        pay_log.append(line)
    out_message = "\n".join(pay_log)
    out_file_name = open(out_file_name, "w")
    print(out_message, file=out_file_name)


def calc_check_sum(isbn):
    formatted_isbn = isbn.replace("-", "")
    check_sum = 0
    for position in range(10):
        value = eval(formatted_isbn[position]) * (10 - position)
        check_sum = check_sum + value
    return check_sum


def send_message(file_name, friend_name):
    message = open(file_name).read()
    friend_file = open("{}.txt".format(friend_name), "w")
    print(message, file=friend_file, end="")


def send_safe_message(file_name, friend_name, key):
    in_message = open(file_name).read()
    new_line = chr(ord("\n") + key)
    out_message = encode(in_message, key).replace(new_line, "\n")
    friend_file = open("{}.txt".format(friend_name), "w")
    print(out_message, file=friend_file, end='')


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_message = open(file_name).read()
    pad = open(pad_file_name).read()
    out_message = encode_better(in_message, pad)
    friend_file = open("{}.txt".format(friend_name), "w")
    print(out_message, file=friend_file)


if __name__ == '__main__':
    pass
