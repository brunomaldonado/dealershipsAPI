brand = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
print("_" * 53)
counter = 1
for l in brand:
    if "e" <= l <="j":
        continue
    if l == "d":
        counter = 4
    print(f"{counter:2} {l}")
    counter += 1