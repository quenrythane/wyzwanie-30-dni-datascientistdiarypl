def switch_case(strng):
    return ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in strng if ch.isalpha())


print(switch_case("Ar./5tUr"))
