from distutils.core import setup
# Multivalued dictionary parameters
# python3 setup.py build
# python3 setup.py sdist
# cat PKG-INFO to see the detail message about mode
# sudo python3 setup.py install
setup(name="package",
      version="1.0",
      long_description="the mode of send and receive message",
      author="lihm",
      author_email="703914503@qq.com",
      url="www.4399.com",
      py_modules=["package.send_message",
                  "package.receive_message"])
