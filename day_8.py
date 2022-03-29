def womensday(name: str) -> str:
    men_name = ["Adama"]
    women_name = ['Abigail']
    if name in women_name or name[-1] == 'a' and name not in men_name:
        return f"Wszystkeigo najlepszego {name}!"
    else:
        return f"Jesteś super {name}"


print(womensday("Adam"))
print(womensday("Adama"))
print(womensday("Zosia"))
print(womensday("Abigail"))
