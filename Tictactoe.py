game_is_on = True
numbers = [1,2,3,4,5,6,7,8,9]

def quest():
    return int(input("Place your marker:"))

def updateboard():
    print("\n")
    print("\t     |     |")
    print(f"\t  {numbers[0]}  |  {numbers[1]}  |  {numbers[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {numbers[3]}  |  {numbers[4]}  |  {numbers[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")    
    print(f"\t  {numbers[6]}  |  {numbers[7]}  |  {numbers[8]}")
    print("\t     |     |")

while game_is_on:
    updateboard()
    rp1 = quest()
    if isinstance(rp1, int) and rp1 in range(1, 10):
        numbers[rp1 - 1] = "X"
        updateboard()
    else:
        break
    rp2 = quest()
    if isinstance(rp2, int) and rp2 in range(1, 10):
        numbers[rp2 - 1] = "O"
        updateboard()
    else:
        break
