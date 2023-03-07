# __name__ params euqal to __main__
# if __name__ = __main__ ,that means run the present function

def say_hello():
    print("hello hello I am say hello")
print(__name__)
# def main():
#     .....
#     pass
# if you want to test mode , __main__
if __name__ == "__main__":
    print(__name__)
    print("test")
    # main()