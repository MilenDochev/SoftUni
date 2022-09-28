string1 = input()
string2 = input()
current_string = string1

for i in range(len(string2)):
    string1[i] = string2[:i] + string2[i] + string2[i:]
    current_string == string1
    if current_string == string1:
        print(string1)