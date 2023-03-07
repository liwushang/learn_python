lista = [3, 5, 7, 9, 11, 13, 12]

listb = [5, 7, 11]

def remove_element_form_list(list1, lsit2):
    listresult = []
    for itema in lista:
        if itema not in listb:
            listresult.append(itema)
    return listresult

outcome = remove_element_form_list(lista, listb)
print(f"remove element form list's outcome is {outcome}")
# print(lista)
def remove_element_form_list1(list1, lsit2):
    listtmp = []
    for i in lista:
        listtmp.append(i)
    # listtmp = lista
    for item in listb:
        listtmp.remove(item)
    return listtmp

outcome1 = remove_element_form_list1(lista, listb)
print(f"remove list:{listb},result is {outcome1}")
# print(lista)
data = [item for item in lista if item not in listb]
print(data)

