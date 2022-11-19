"""
Simple script to practice: for loop, try/except, dictionary collection.
In Czech, english version is not available.
"""

# Načtěte text od uživatele a na výstup vytiskněte slovník,
# kde každý klíč reprezentuje písmeno v načteném textu
# a jeho hodnota je počet daných písmen v načteném textu.

vstup = input("Zadej retezec\n").lower()

slovnik_znaku = {}
for znak in vstup:
    if znak.isalpha():
        try:
            slovnik_znaku[znak] += 1
        except KeyError:
            slovnik_znaku[znak] = 1

print(slovnik_znaku)