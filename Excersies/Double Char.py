strint_received = ""
while True:
    strint_received = input()
    if strint_received == "End":
        break
    if strint_received != "SoftUni":
        for i in range(0, len(strint_received)):
            print(strint_received[i], end="")
            print(strint_received[i], end="")
    else:
        continue
    print(end="\n")