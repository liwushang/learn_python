"""
tools about string
"""


def str_reverse(s):
    """
    reverse string
    :param s: the string to be reverse
    :return: the reversed string
    """
    return s[::-1]


def substr(s, x, y):
    """
    according to the designated index to finish string slices
    :param s: the string to be slices
    :param x: the start index
    :param y: the end index
    :return: the splited string
    """
    return s[x:y:1]


if __name__ == '__main__':
    print(str_reverse("hello world"))
    print(substr("hello world", 3, 13))

