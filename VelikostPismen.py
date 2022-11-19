"""
Simple script to practice: users's input, for loop, if / elif statement, strings methods.
In Czech, english version is not available.
"""

# Načtěte text od uživatele a zjistěte,
# jestli se v textu nachází nějaké malé nebo nějaké velké písmeno nebo oboje
# (velké i malé písemeno) a vypište výsledek na výstup.

print("Napište text.")
text = input()
#print(type(text))
seznam_pismen = [text]
#print(type(seznam_pismen))

for pismeno in seznam_pismen:
    if pismeno.isupper() == True and pismeno.islower() != True:
        print("Text obsahuje velká písmena.")

    elif pismeno.islower() == True and pismeno.isupper() != True:
        print("Text obsahuje malá písmena.")

    elif pismeno.isupper() == False and pismeno.islower() == False:
        print("Text obsahuje malá i velká písmena.")

    elif pismeno.isupper() != False and pismeno.islower() != False:
        print("Text neobsahuje ani malá, ani velká písmena.")


print("Konec.")
