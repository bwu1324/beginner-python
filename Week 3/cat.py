# i = 0
# while i < 3:
#     print("meow")
#     i += 1 # i = i + 1

# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end='')

# while True:
#     n = int(input("What's n? "))
#     if n >= 0:
#         break


# while n > 0:
#     print("meow")
#     n -= 1


def main():
    num_meows = get_positive_number("Enter the number of meows you want: ")
    for _ in range(num_meows):
        print("meow")


def get_positive_number(prompt = "Enter a positive number: "):
    while True:
        n = int(input(prompt))
        if n > 0:
            return n
        print("Try again")

main()