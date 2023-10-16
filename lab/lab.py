# Символ, який буде відображатися на полі
symbol = ". . . . . . . . . . . .\n\
. X . X . . . . . . . .\n\
. . X . . . . . . . . .\n\
. X . X . . . . . . . .\n\
. . . . . . . . . . . .\n\
. . . . . . . . . . . .\n\
. . . . . . . . . . . .\n\
. . . . . . . . . . . .\n\
. . . . . . . . . . . .".replace(" ", '')
def display_field(dx, dy, symbol):
    coords = []
    dxy = dx + dy*13
    print(f"{symbol}\n")

    for i in range(symbol.count("X")):
        coords += [symbol.find("X")]
        symbol = symbol.replace("X", '.', 1)
    coords = [coords[i]+dxy for i in range(len(coords))]
    symbol = [i for i in symbol]
    for i in coords:
        symbol[i] = "X"
    print("".join(symbol))
def enter_coords():
    try:
        dx = int(input("Введіть відстань по горизонталі (0 для виходу): "))
        dy = int(input("Введіть відстань по вертикалі (0 для виходу): "))
    except ValueError:
        print("Введіть коректні дані!!!")
        return enter_coords()
    return dx, dy

coords = enter_coords()
display_field(coords[0], coords[1], symbol)
