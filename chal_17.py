bankAccount = 0
while True:
    action = str(input("Enter 'D' for deposit or 'W' for withdrawal followed by a white-space and the amount of $: "))
    action = action.split()
    if action[0] == 'D':
        bankAccount += int(action[1])
    else:
        bankAccount -= int(action[1])
    finish = input("Are you done? Y/N\n")
    if finish == 'Y':
        break
    else:
        pass

print(f"net bank account ($): {bankAccount}")
