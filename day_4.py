def gerund_infinitive(strng: str) -> str:
    if strng.endswith('ing'):
        return f"to {strng[:-3]}"
    else:
        return "to nie jest rzeczownik odsłowny"

# do
print(gerund_infinitive("a"))
print(gerund_infinitive("doing"))
# print("a"[-3])


