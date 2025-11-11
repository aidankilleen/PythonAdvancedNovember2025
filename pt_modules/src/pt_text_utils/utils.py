# utils.py
import pyfiglet


# some text utilities


def pt_word_count(text):
    words = text.split()
    return len(words)


def intro():
    f = pyfiglet.figlet_format("Welcome to pt_text_utils", font="slant")
    print(f)
