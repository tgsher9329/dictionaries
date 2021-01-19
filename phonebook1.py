phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

who = input("Who would you like to look up?")
print(phonebook_dict[who])

# ---------------------- Add a number

phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

# ------------------- delete alices number

del phonebook_dict['Alice']

# --------------------- change bob number to 968-345-2345

phonebook_dict['Bob'] = '968-345-2345'

# ----------------------

print(phonebook_dict)