contact_info = {
    "Alice": "1233-1321",
    "Bob": "123123123"
}

print(contact_info)

alice_phone = contact_info["Alice"]
print(alice_phone)

#Update Alices's phone number
contact_info['Alice'] = "12313"
print(contact_info)

#Add a new Contact

contact_info["Eve"] = "555-1233"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

#.keys()
keys = contact_info.keys()
print(keys)

#get the values
values = contact_info.values()
print(values)

#get the items
items = contact_info.items()
print(items)