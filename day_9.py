def mid(strng: str) -> str:
    if len(strng) % 2:
        return strng[len(strng)//2]
    else:
        return ""


print(mid("abcde"))
print(mid("abcdef"))
