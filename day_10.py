from random import choices, choice
from string import ascii_lowercase

list_samo = "aeiouy"
def name_gen(l_name: int, l_surname: int) -> str:
    # raz spolgłoska raz samogloska
    # nie kończy się na -a
    name = ""
    for ch in range(l_name):
        samo_counter = len([ch for ch in name if ch in "aeiouy"])
        if samo_counter * 2> len(name) - samo_counter:
            name += choice(ascii_lowercase)

        if len(name) == l_name:
            while name[l_name-1] == "a":
                name[l_name-1] += choice(ascii_lowercase)



    return name


print(name_gen(6, 6))
