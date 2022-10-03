Name = ""
while True:
    Name = input()
    if Name == "Voldemort":
        print("You must not speak of that name!")
        break
    if Name == "Welcome!":
        break
    if len(Name) < 5:
        print(f"{Name} goes to Gryffindor.")
    elif len(Name) == 5:
        print(f"{Name} goes to Slytherin.")
    elif len(Name) == 6:
        print(f"{Name} goes to Ravenclaw.")
    elif len(Name) > 6:
        print(f"{Name} goes to Hufflepuff.")

if Name != "Voldemort":
    print('Welcome to Hogwarts.')

