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
            new_text += "\n\n"
        if char in indent_chars and text[index]
            extract = text[index:].strip()
            new_text += extract

    print(new_text)

