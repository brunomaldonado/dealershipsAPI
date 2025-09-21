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

print("\n\n")


import textwrap

def textwrap_message(message):
    max_width = 48  # límite de ancho
    wrapped_title = textwrap.fill(
        message,
        width=max_width,
        initial_indent=" ",      # la primera línea arranca con un espacio
        subsequent_indent=" "    # las demás líneas igual, alineadas a la izquierda
    )
    return wrapped_title


# Ejemplo
msg = "The Motorcycle BMW R 1250 GS Adventure Enduro / offroad has been added to the inventory."
print(textwrap_message(msg))

  
