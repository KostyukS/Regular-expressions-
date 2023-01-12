import edit

if __name__ == "__main__":
    file = "phonebook_raw.csv"
    file1 = "phonebook1_raw.csv"

    contacts_list = edit.create_contact_list(file)
    contacts_list_new = edit.edit_name_telephone(contacts_list)
    unic_list = edit.unic_list(contacts_list_new)
    edit.create_new_unic_list(file1, unic_list)
