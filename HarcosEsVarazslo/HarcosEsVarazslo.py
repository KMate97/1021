import random

Harcos = random.randint(0,9)
Varazslo = random.randint(0,9)
mezo = random.randint(1,3)
harc = random.randint(1,6)
harcos_mezo = random.randint(1,3)
varazslo_mezo = random.randint(1,3)

print("A harcos és a varázsló megküzd.")

if harcos_mezo == varazslo_mezo:
    if harc