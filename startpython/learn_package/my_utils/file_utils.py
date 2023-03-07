"""
tools abot file
"""

def print_file_info(file_name):
    """
    print the designated file content in console
    :param file_name: the file path to be read
    :return: None
    """
    f = None
    try:
        f = open(file_name,"r")
        content = f.read()
        print("the file content just as follows:")
        print(content)

    except Exception as e:
        print(f"the program meets exception, the reason is {e}")

    finally:
        if f:
         f.close()


def append_to_file(file_name, data):
    """
    append the designated data to the designated file
    :param file_name: the designated file path
    :param data: the designated data
    :return: None
    """
    f = open(file_name, "a")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("/home/liwushang/PycharmProjects/pythontest1/a.txt")
    append_to_file("/home/liwushang/PycharmProjects/pythontest1/a.txt", "dashabi")