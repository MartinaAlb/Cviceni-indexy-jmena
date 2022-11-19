"""
First calculator, basic math. operations.
In Czech, english version is not available.
"""

print("Zadejte první číslo")
prvni_cislo = input()

try:
    prvni_cislo = float(prvni_cislo)
except:
    print("Nebylo zadano číslo, program končí")
    exit()

print("Zadejte druhé číslo")
druhe_cislo = input()

try:
    druhe_cislo = float(druhe_cislo)
except:
    print("Nebylo zadano číslo, program končí")
    exit()

print("Zadej jednu z těchto operací +, - , *, /")
operace = input()


if operace == "+":
    vysledek = prvni_cislo + druhe_cislo
elif operace == "-":
    vysledek = prvni_cislo - druhe_cislo
elif operace == "*":
    vysledek = prvni_cislo * druhe_cislo
elif operace == "/":
    if druhe_cislo == 0:
        print("Nelze dělit číslem 0!")
        exit()
    vysledek = prvni_cislo / druhe_cislo
else:
    vysledek = "Nic, nebyla zadaná podporovaná operace"

print(f"Výsledek výpočtu je {vysledek}")

print("Konec")