import random

Harcos_Hp = random.randint(1, 9)
Varazslo_Hp = random.randint(1, 9)
Harcos_Mezo = random.randint(1, 3)
Varazslo_Mezo = random.randint(1, 3)

print("A harcos es a varazslo elindult a harcba!")

if Harcos_Mezo == Varazslo_Mezo:
    print("A harcos es a varazslo talalkozott!")
    Sebzes = random.randint(1, 6)
    Valasztas = random.randint(1, 2)
    print("A harc elkezdodik!")
    if Valasztas == 1:
        print("A harcos tamad eloszor!")
        print(f"A harcos sebzese: {Sebzes}, es HP-ja: {Harcos_Hp}")
        print(f"A varazslo HP-ja: {Varazslo_Hp}")
        Varazslo_Hp -= Sebzes
        if Varazslo_Hp < 0:
            Varazslo_Hp = 0
        print(f"A varazslo HP-ja harc utan: {Varazslo_Hp}")
    else:
        print("A varazslo tamad eloszor!")
        print(f"A varazslo sebzese: {Sebzes}, es HP-ja: {Varazslo_Hp}")
        print(f"A harcos HP-ja: {Harcos_Hp}")
        Harcos_Hp -= Sebzes
        if Harcos_Hp < 0:
            Harcos_Hp = 0
        print(f"A harcos HP-ja harc utan: {Harcos_Hp}")
else:
    print("A harcos es a varazslo nem talalkozott. A harc elmarad.")