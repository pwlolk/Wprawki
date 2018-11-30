#Rysowanie listy

print("Tabliczka mnożenia".upper())

def mult_table (size_x, size_y):
    cell_size = len(str(size_x) + "x" + str(size_y) + "=" + str(size_x*size_y))
    cell_size += 2

    if (size_x == 2 and size_y == 2):
        print("+" + size_x*(cell_size*"-" + "+"))
        for x in range(1, size_x+1):
            for y in range(1, size_y+1):
                if (y == 1):
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x * y)).center(cell_size), end="")
                else:
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x * y)).center(cell_size) + "|")
        print("+" + size_x * (cell_size * "-" + "+"))
    else:
        print("+" + size_y * (cell_size * "-" + "+"))
        for x in range(1, size_x+1):
            for y in range(1, size_y+1):
                if (y==1):
                    print("|" + (str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|", end = "")
                elif (y > 1 and y < size_y):
                    print((str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|", end = "")
                else:
                    print((str(x) + "x" + str(y) + "=" + str(x*y)).center(cell_size) + "|")
        print("+" + size_y * (cell_size * "-" + "+"))

size_x = int(input("Podaj rozmiar tabeli w pionie [min.2]: "))
size_y = int(input("Podaj rozmiar tabeli w poziomie [min.2]: "))
mult_table(size_x, size_y)