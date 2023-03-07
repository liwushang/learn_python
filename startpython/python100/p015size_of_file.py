import os

path_dict = {}
for file in os.listdir("."):
    if os.path.isfile(file):
        size = os.path.getsize("{}".format(file))
        path_dict[file] = size
sort_result = sorted(path_dict.items(), key = lambda x:x[1], reverse=True)
# print(path_dict)
# print(sort_result)
# print(len(sort_result))
#
# for item in sort_result:
#     if "ceshi" in item:
#         print("doc exist")

