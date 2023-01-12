import re
import os
import csv


def edit_name_telephone(contacts_list):
    contacts_list_new =  []
    contacts_list_new.append(contacts_list[0])
    pattern = r"(\+7|8)[\s|\-]*\(*(\d{3})\)*[\s|\-]*(\d{3})[\s|\-]*(\d{2})[\s|\-]*(\d{2})\s*\(*(доб.)*\)*\s*(\d+)*\)*"
    for item in contacts_list[1:]:
        lst = ['', '', '', ]
        str = ' '.join(item[0:3])
        lst_1 = str.split()
        for var in range(len(lst_1)):
            lst[var] = lst_1[var]
        del item[0:3]
        lst_2 = lst + item
        lst_2[5] = re.sub(pattern, r"\1(\2)\3-\4-\5 \6\7", item[2])
        contacts_list_new.append(lst_2)
    return contacts_list_new


def unic_list(contacts_list_new):
    buf_list = []
    for item in contacts_list_new:
        buf_list.append(item[0:7])
    for item in buf_list:
        for var in contacts_list_new:
            if item[0] == var[0] and item[1] == var[1]:
                for i in range(len(var)):
                    if var[i] != '' and item[i] == '':
                        item[i] = var[i]
    unic_list = []
    for item in buf_list:
        if item not in unic_list:
            unic_list.append(item)
    return unic_list


def create_contact_list(file):
    path = os.path.abspath('Text/' + file)
    with open(path, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def create_new_unic_list(file, unic_list):
    with open(file, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(unic_list)