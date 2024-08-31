def double_string(string):
    sentence = []
    for character in string:
        double = character + character
        sentence.append(double)
    doubled_sent = "".join(sentence)
    return doubled_sent      