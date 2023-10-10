#!/usr/bin/python3
"""Contains a function that write a text to filename.txt 
    and save it.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
        returns the number of characters written
        Args:
            filename (str): name of the file
            text (str): what to write
        Returns:
            int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
        return count

if __name__ == "__main__":
    nb_characters = write_file(
        "my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
