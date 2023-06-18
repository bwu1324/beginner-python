def main():
  # Get the user's name
  name = input("What is your name? ")
  greet(name)

def greet(to = "World"):
  # Clean up the formmating by removing extra spaces and capitalizing i
  to = to.strip().title()

  # Print it out
  print(f"Hello, {to}!") 

main()
