import os
# when you call the .read() method,
# the pointer comes to the end of file

# file = open("readme")
# print(file.read())
# print(file.read())
# file.close()

# the function .open() default to read-only mode
# f = open("file", "manner of open file")

# file = open("readme", "w")
# file.write("hello")

# file_new = open("readme")
# "w"the origin content will be covered
# "a"the method of append elements to the file
# "r+","w+","a+" open the file with method of read and write
# file_new.write("hello")
# print(file_new.read())
# print(file.read())
# file_new.close()

# the second method of read files:readline
# file = open("readme")
# while True:
#     text = file.readline()
#     if not text:
#         break
#     print(text)
# file.close()


# copy the file "readme" to a new file
# small file
# file_read = open("readme")
# file_write = open("readme_copy", "w")
# text = file_read.read()
# file_write.write(text)
# file_read.close()
# file_write.close()

# large file
# file_read = open("readme")
# file_write = open("readme_copy1", "w")
# while True:
#     test = file_read.readline()
#     if not test:
#         break
#     file_write.write(test)
# file_read.close()
# file_write.close()


# import os
# os.rename os.remove os.listdir os.mkdir
# os.remove("readme_copy1")
# os.mkdir("test1")
# os.rmdir("test1")
