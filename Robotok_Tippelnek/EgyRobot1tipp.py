import random

nagy_robot = random.randint(1, 10)
probalkozas = 0

print("A nagy robot gondolt egy számra 1 és 10 között!")

while True:
    robot1 = random.randint(1, 10)
    robot2 = random.randint(1, 10)
    robot3 = random.randint(1, 10)

    probalkozas += 1

    print("1. robot tippje:", robot1)
    print("2. robot tippje:", robot2)
    print("3. robot tippje:", robot3)

    if robot1 == nagy_robot or robot2 == nagy_robot or robot3 == nagy_robot:
        print("Az egyik kis robot eltalálta a számot!")
        print("A nagy robot száma:", nagy_robot)
        print("Próbálkozások száma:", probalkozas)
        break

eletkor = int(input("Add meg az életkorodat: "))
kartya = input("Van belépőkártyád? (igen/nem): ")

if eletkor >= 18:
    if kartya == "igen":
        print("Beléphetsz.")
else:
    print("Túl fiatal vagy a belépéshez.")