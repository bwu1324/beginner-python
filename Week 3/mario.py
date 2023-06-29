def print_col(n):
    for _ in range(n):
        print("#")


def print_row(n):
    for _ in range(n):
        print("?", end='')
    print()


def print_square(n):
    for row in range(n):
        for col in range(n):
            print("#", end='')
        print()


def print_triangle(n):
    for row in range(n):
        for col in range(row + 1):
            print("#", end="")
        print()
    


print_triangle(233)
