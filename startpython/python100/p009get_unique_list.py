def get_unique_list(argslist):
    listb = []
    for items in argslist:
        if items not in listb:
            listb.append(items)
    return listb


lista = [10, 20, 30, 10, 20]

print(f"source list{lista}, unique list:", get_unique_list(lista))

# set = collection
print(f"source list{lista}, unique list:", list(set(lista)))
