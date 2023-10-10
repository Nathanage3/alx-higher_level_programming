#!/usr/bin/python3
"""Contains a function that write a text to filename.txt 
    and save it.
"""


def write_file(filename="", text=""):
    """ Write a string to a text file (UTF-8) and return the number of characters written.

        Args:
            filename (str): a filename
            text (str): a text file
        Returns:
            number of chars
    """
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
        return count

if __name__ == "__main__":
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
