import os


search_dir = os.getcwd()
high_level = os.path.split(search_dir)[0]
print(high_level)
result_files = []
path_dict = {}
for root, dirs, files in os.walk(high_level):
    # print(f"root:{root}, dirs:{dirs}, files:{files}")
    for file in files:
        file_path = f"{root}/{file}"
        # print(file_path)
        result_files.append((file_path, os.path.getsize(file_path)/1000))
        size = os.path.getsize(file_path)
        path_dict[file_path] = size/1000

sort_result = sorted(path_dict.items(), key =lambda x:x[1], reverse=True)[:10]
print(sort_result)
sort_result1 = sorted(result_files, key = lambda x:x[1], reverse=True)[:10]
print(sort_result1)
