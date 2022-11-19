"""
Simple script to practice: user's input, data type, string indexes,
if/elif statements, f/strings.
In Czech, english version is not available.

"""

# Nactete vstup od uzivatele, pokud je vstup cislo, vynasobte jej dvema,
# pokud se jedna o text delsi jak 10 znaku, vytisknete jeho predposledni znak,
# pokud je text delsi jak 5 znaku, vytisknete prvni a treti znak.

print("Napiš svůj vzkaz - text nebo číslo")
vzkaz = input()

try:
    vzkaz = float(vzkaz)
    print(f"Dvojnásobek tvého čísla je {vzkaz * 2}")
except:
    pass



if type(vzkaz) == str:
    if len(vzkaz) > 10:
        print(f"První a třetí znak vzkazu je {vzkaz[0]} a {vzkaz[2]}.")
        print(f"Předposledním znakem vzkazu je {vzkaz[-2]}.")
    elif len(vzkaz) < 5:
        print("Tvůj vzkaz je moc krátký, začni znovu a napiš delší")
    else:
        print(f"První a třetí znak vzkazu je {vzkaz[0]} a {vzkaz[2]}.")




print("Díky, to je vše.")