# x = int(input("What is x? "))
# y = int(input("What is y? "))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# Short circuting

x = 10
y = 0


if y != 0 and x / y > 0: # x/y will never be executed because y != 0 is already false, the condition can never be true so python moves on
    print("do a thing")


name = input("What's your name? ")


# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # Undercore is the default if nothing else matches
        print("Who?")

