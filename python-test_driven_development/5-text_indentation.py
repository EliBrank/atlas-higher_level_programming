#!/usr/bin/python3

"""defines the function text_indentation"""


def text_indentation(text):
    """prints input string with newlines after '.' '?' and ':' characters

    Args:
        text: string to eval and add potential newlines to
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent_chars = ('.','?',':')

    new_text = ""

    for index, char in enumerate(text):
        if char in indent_chars:
            new_text += char + "\n\n"
        elif text[index].isspace() and new_text[-1] == '\n':
            continue
        else:
            new_text += char


    print(new_text, end="")

