"""
Simple script to practice: user's input, string indexes, string formating.
In Czech, english version is not available.
"""

print("Napiš svoje jméno")
jmeno = str(input())
print("Napiš svoje příjmení")
prijmeni = str(input())

# kontrola datového typu
print(type(jmeno))
print(type(prijmeni))

# prvni_pismeno
print(f"Tvoje jméno začíná na písmeno {jmeno[0]}")
print(f"Tvoje příjmení začíná na písmeno {prijmeni[0]}")

# znak na 5 a 6 místě
if len(jmeno) >= 5:
    print(f"5. a 6. písmeno tvého jména jsou {jmeno[4:6]}")
else:
    print("Tvoje jméno má méně než 6 písmena")

if len(prijmeni) >= 5:
    print(f"5. a 6. písmeno tvého příjmení jsou {prijmeni[4:6]}")
else:
    print("Tvoje příjmení má méně než 6 písmena")

# poslední dvě písmena / dvě možnosti negativního indexování
print(f"Tvoje jméno končí na písmena {jmeno[-2:]}")
print(f"Tvoje příjmení končí na písmena {prijmeni[-2]}{prijmeni[-1]}")

# iniciály (možné i bez teček mezi písmeny)
print(f"Tvoje iniciály jsou {jmeno[0]}.{prijmeni[0]}.")

# délka jména
if len(jmeno) == 1:
    print(f"Tvoje jméno má {len(jmeno)} znak")
elif len(jmeno) <= 4:
    print(f"Tvoje jméno má {len(jmeno)} znaky")
else:
    print(f"Tvoje jméno má {len(jmeno)} znaků")

# jméno a příjmení malými a velkými písmeny
jmeno_velkym = jmeno.upper()
print(f"Takhle vypadá tvoje jméno napsané velkými písmeny {jmeno_velkym}")
prijmeni_malym = prijmeni.lower()
print(f"Takhle vypadá tvoje příjmení napsané malými písmeny {prijmeni_malym}")

# index znaku
print("Máš ve svém jméně písmeno 'a'?")
hledane_pismeno = 'a'
try:
    index_znaku = jmeno.index(hledane_pismeno)
    print(f"Písmeno '{hledane_pismeno}' je ve tvém jméně na indexu {index_znaku}.")
except:
    print(f"Ve svém jméně nemáš '{hledane_pismeno}'.")

# celé jméno, spojení jména a příjmení pomocí .join
cele_jmeno = (" ".join([jmeno, prijmeni]))
print(f"Tvoje jméno a příjmení je {cele_jmeno} ")
print("--------")
print("To je vše o tvém jméně")
