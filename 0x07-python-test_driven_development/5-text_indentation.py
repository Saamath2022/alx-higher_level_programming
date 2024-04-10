def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']

    for char in text:
        print(char, end='')

        if char in new_line_chars:
            print("\n" * 2, end='')
