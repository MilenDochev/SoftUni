list_of_phones = input().split(", ")
command = ""
for i in range(len(list_of_phones)):
    command = input()
    if command == "End":
        break
    if "Add" in command:
        last_element = command.split(" ")
        phone = last_element[-1]
        if list_of_phones.count(phone) == 0:
            list_of_phones.append(phone)

    if "Remove" in command:
        last_element = command.split(" ")
        phone = last_element[-1]
        if list_of_phones.count(phone) == 1:
            list_of_phones.remove(phone)
        else:
            continue
    if "Bonus phone" in command:
        last_element = command.split(" ")
        phone = last_element[-1]
        old_new = phone.split(":")

        if list_of_phones.count(old_new[0]) == 1:
            a = list_of_phones.index(old_new[0])
            list_of_phones.insert(a+1, old_new[1])
        else:
            continue

    if "Last" in command:
        last_element = command.split(" ")
        phone = last_element[-1]
        if list_of_phones.count(phone) == 1:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)

x = ", ".join(list_of_phones)
print(x)