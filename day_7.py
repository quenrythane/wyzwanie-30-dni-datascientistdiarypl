def capital_indexes(strng: str) -> list[int]:
    return [i for i, ch in enumerate(strng) if ch.isupper()]


print(capital_indexes("AdAm"))
