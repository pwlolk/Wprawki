#Rysowanie listy

print("\nTabliczka mnożenia [współrzędne]\n".upper())

def mult_table_reversed (size_x, size_y):
    cell_size = len(str(size_x) + "x" + str(size_y) + "=" + str(size_x*size_y))
    cell_size += 2
    if (size_x == 2 and size_y == 2):
        print("+" + size_y*(cell_size*"-" + "+"))
        for y in range(size_y, 0, -1):
            for x in range(1, size_x+1):
                if (x == 1):
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x * y)).center(cell_size), end="")
                else:
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x * y)).center(cell_size) + "|")
        print("+" + size_y * (cell_size * "-" + "+"))
    else:
        print("+" + size_x * (cell_size * "-" + "+"))
        for y in range(size_y, 0, -1):
            for x in range(1, size_x+1):
                if (x==1):
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|", end = "")
                elif (x > 1 and x < size_x):
                    print((str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|", end = "")
                else:
                    print((str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|")
        print("+" + size_x * (cell_size * "-" + "+"))

size_x = int(input("Podaj rozmiar tabeli w poziomie(x) [min.2]: "))
size_y = int(input("Podaj rozmiar tabeli w pionie(y) [min.2]: "))
mult_table_reversed(size_x, size_y)