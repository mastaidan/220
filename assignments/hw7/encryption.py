def encode(message, key):
    message_length = len(message)
    uni_message = []
    coded_message = []
    for index in range(message_length):
        coded_value = ord(message[index]) + key
        uni_message.append(coded_value)
        coded_chr = chr(uni_message[index])
        coded_message.append(coded_chr)
    return "".join(coded_message)


def encode_better(org_message, org_key):
    message_length = len(org_message)
    key_length = len(org_key)
    number_message = []
    number_key = []
    coded_ord_message = []
    coded_message = []
    for index in range(key_length):
        number_letter = ord(org_key[index]) - 65
        number_key.append(number_letter)
    for index in range(message_length):
        number_letter = ord(org_message[index]) - 65
        number_message.append(number_letter)
        coded_number = number_message[index] + number_key[index]
        coded_ord_message.append(coded_number)
        number = coded_ord_message[index] % 58
        letter = chr(number + 65)
        coded_message.append(letter)
    return "".join(coded_message)
