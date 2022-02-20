"""
Name: Aidan Mast
hw5.py

Problem: Format strings and list and output various information and codes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first last): ")
    name_split = name.split()
    print(name_split[1], end=", ")
    print(name_split[0])


def company_name():
    name = input("enter a domain:")
    name_split = name.split(".")
    print(name_split[1])


def initials():
    students = eval(input("how many students are in the class?"))
    for i in range(students):
        question = "what is the name of student " + str(i + 1) + "?"
        name = input(question)
        name_split = name.split()
        first_name = name_split[0]
        last_name = name_split[1]
        first_init = first_name[0]
        last_init = last_name[0]
        initial = first_init + last_init
        print(initial)


def names():
    name_list = input("enter a list of names: ")
    split_list = name_list.split(",")
    number = len(split_list)
    for i in range(number):
        name = split_list[i].split()
        first_name = name[0]
        last_name = name[1]
        first_init = first_name[0]
        last_init = last_name[0]
        print(first_init, end="")
        print(last_init, end=" ")


def thirds():
    number = eval(input("enter the number of sentences: "))
    sentences = []
    for i in range(number):
        inst = "enter sentence " + str(i + 1) + ":"
        sentence = input(inst)
        sentences.append(sentence)
    for j in range(number):
        sentence = sentences[j]
        characters = len(sentence)
        index = round((characters + 1) / 3)
        for k in range(index):
            print(sentence[k * 3], end="")
        print()


def word_average():
    sentence = input("enter a sentence: ")
    words = sentence.split()
    length = len(words)
    total = 0
    for i in range(length):
        letters = len(words[i])
        total = total + letters
    print(total / length)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin")
    words = sentence.split()
    length = len(words)
    pig_sentence = ""
    for i in range(length):
        word = words[i]
        characters = len(word)
        first_letter = word[0]
        pig_word = word[1:characters] + first_letter + "ay"
        pig_sentence = pig_sentence + pig_word + " "
    print(pig_sentence.rstrip().lower())


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
