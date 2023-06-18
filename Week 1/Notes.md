# Week 1 Python, Functions, and Variables

## What is python?
* Python is a program whos job is to read python `syntax` (def. the arrangement of words and phrases to create well-formed sentences in a language) and instruct the computer to do what that python syntax means.
* This type of program is known as an `interpreter`
	* This is why it is important to learn the syntax (the rules) of how to write code. If your syntax is incorrect, python will not understand what you want it to do and will error
* To run a python program in the command line, you use the command:
	```powershell
	python <name of your python file>
	```
	* First "python" tells your computer to look from the program "python" installed on your computer
	* The next term is your python file, this tells python which file it should open up and read

* **When we are writing a python program, we are creating a text file that contains the set of instructions, written in a specific way, for python to read and execute**
* You can write python programs using `Notepad`, or something similar.
* However, we can use a different text editor that will make it a little easier and faster to write and debug code:
	* For example, `Idle`, `PyCharm`, `Vim`, `Sublime Text`, etc.
* We are going to use `VS Code`
	* Out of the box, it is basically just a text editor + a file browser + command line
	* We can install extensions for python (I'm going to use the Microsoft `Python` and `Pylance` extensions)
	* This will now give us a text editor with some extra features such as:
		* syntax highlighting - notice how different parts of the program is colored differently depending on if it is a function, a variable, or something else
		* autocomplete - as you type, VS Code will give you suggestions based on what it sees in your program
		* formatting - if you hit `alt + shift + f`, VS Code will reformat your text file so it looks nicer (doesn't change what the code does though)
		* and more...


## "Hello, World"

### How do we create a python program?
* To create a python program, let's start by creating a file called `hello.py`
	* `.py` tells the computer, this file contains a python program. However, remember that this is actually just a text file. You can create a python program as `hello.txt` and run `python hello.txt` and it will work just as well

* Open the file up and add in:
```python
print("Hello, World")
```
* Run the program running in the command line:
	```
	python hello.py
	```
	* What happens?

## What are functions?
* Something that tells the computer to do something
* A function can take in `arguments` which the function can use to change it's behavior
* Function can have `side effects` or things that happens when a function is run
* Most languages have some function built in
	* For example, python has `print()` to print something out on the command line
		* It can take an `argument` which changes what specifically it will print out
		* It has a `side effect` which is that something gets printed out to the screen
	* Refer to: https://docs.python.org/3/library/functions.html for built in python functions
* `bugs` are problems with your code that causes it to do something unintended
	* For example, if you remove the closing parenthesis, the program will crash

## Reading Python Documentation
* Let's take a look at the documentation of `print()`

> print(*objects, sep=' ', end='\n', file=None, flush=False)

* When we are using a function we call the things we pass in `arguments`
* when we are taking about defining a function we call them `parameters`
* Print has a number of parameters:
	* `*objects` - A positional parameter
		* The star (*) indicates that you can have any number of these paramters (including none of them -> `print()` works!)
		* So you can do something like `print("Hello", "World")`
		* This means that the order of these paramters matters, you must pass then in in order (`print("Hello", "World")` is not the same as `print("World", "Hello")`)

	* `sep=' '` - A named paramter
		* You can pass these in in any order, provided that it is after all of  the positional parameters (`print("Hello", "World", sep=', ')` works but `print(sep=', ', "Hello", "World")` will not)
		* These are also optional, you don't have to pass them in. The equal sign tells you what the default value will be, in this case the default value for `sep` is `' '`, a space

## We have output, what about input?
* One way we can take input to our program is through using the `input()` function like so:
* The `input()` function `returns` what the user types in when they hit enter.

```python
name = input("What is your name?: ")

print("Hello,", name)
```
* Notice the equal sign.
	* This is the `assignment operator` it *assigns* the return value of `input()` into `variable` named `name`
		* The assignment operator always assigns from right to left
	* A `variable` is basically a named container for data. In this program we are creating a variable with the name `name` and storing the user's input into it


## Methods
* Different types of data also have special functions attached to them
* The return value of `input()` is what is known as a `str` or `string`
* In python `str` have special functions that we can call such as `strip()`, and `title()`
* These special functions are called `methods` and are always attached to specific types of data
* We call these `methods` by using dot\<name of function\>
```python
name = name.strip()
name = name.title()
```
* Tip: Since name.strip() returns a `str`, we can actually chain these functions together
```python
name = name.strip().title()
```
* This can help you shorten your code but use it sparingly because it can also make it harder to understand
* Take a look at the python documation of `str` to see all the python-defined methods

## Concatonation and F-strings
* One way we could print out "Hello, \<name\>" was by passing in multiple strings into the `print()` function
* Another way is called concatonation
	* Concatonation is where you combine two strings by putting one after another
	* We do this using the `+` symbol (`#` denotes a comment which are used to explain our code but are ignored by python)
	```python
	name = input("What is your name? ") # Assume we enter "Bennett"
	combined = "Hello, " + name # combined = "Hello, Bennett"
	print(combined)
	```
* We can also create strings that depend on another variable another way using `f-strings`
	* We do this by creating a string normally, then typing `f` in front of the string, then any variables we want to place into the string, we use the `{}` curly braces
	```python
	name = input("What is your name? ") # Assume we enter "Bennett"
	print(f"Hello, {name}") # "Hello, Bennett"
	```
	* Instead of printing literally, "Hello, {name}", the f-string is going to replace the "{name}" with the value of the variable name
	* Do take a look at the f-string documentation for more things f-string can do (they can format numbers in a specific way, dates and more)

## Excaping strings
* String are defined in python using single (') or double (") quotes, what if you want to print out a single or double quote?
	* We use the "\" characters
	* This is an `excape` character, it tells python that the next character should be treated specially. For example, 
		* `"\""` tells python that this string contains a double quote
		* `"\n"` tells python that this string contains a new line and not literally \n
		* `"\\"` tells pthon that this string contains a **single** backslash
		* `"\t"` tells python that this string contains a tab
	* In f-strings we can use curly braces by typing `"{{"` or `"}}"` for one curly brace

## Integers and Operations
* An `int` is data type that contains integers (-10, -1, 0, 1, 10, 100)
* We can do a number of operations with integers: `+, -, /, *, %`
	* `+` adds the numbers
	* `-` subtracts the numbers
	* `/` divides the numbers and resutls in a `float` which is a floating point number which contains decimal numbers
		* Floats can do the same operations as int but have a little more complexity which we will talk aobut later
	* `%` takes the modulus of the numbers also known as the remainder after dividing
* We can assign an integer simply using:
```python
my_number = 10
```
* However, if we want to take this value from the user, we need to convert the `str` we get from the input function and turn it into an `int`.
* Python has a built in function to do this called `int()`
```python
x = int(input("What is x? "))
```
* Now we can play around with integers:
```python
x = int(input("What is x? "))
y = int(input("What is y? "))

z = x / y # try some different operations

print(z)
```

## Defining Custom Functions
* What if we want to make our own custom functions?
* We can do so using the `def` keyword like this:
	```python
	def my_function(x, y = 1):
		print("Doing something")
		return a + y
	```
	* `def` indicates to python we are creating a function
	* `my_function` is the name of your new function
	* `(x, y = 2)` is the parameter list of the function
		* `x` tells us we have 1 required positional argument
		* `y = 1` tells us we have 1 optional named argument 
	* `:` is required to define a function and tells python to expect and indentation
	* Notice how the body of the function is indented by 1, this is required for python in order for python to know what lines of code are part of the function and what is not
	* The `return` keyword is used to return a value from a function. It is optional if you are not returning anything
* One problem we might run into is that functions must be defined *before* they are used
```python
use_me() 	# Causes error

def use_me():
	return 0

use_me() # Works
```
* As our programs get more complicated, this can get messy because we are going to have files that are full of function definitions at the top and our main code at the bottom
* One way to get around this is a pattern like this:
```python
def main():
	print("Do some stuff here")  # Define a main function where our main code is

	some_function("Call Some Functions") # Our main code might call some other functions


def some_function(t): # Define our functions under the main function
	print(t)

main() # Remember the to all the main function at the very bottom
```
* This way all of our functions are going to be defined when our main code runs and we have our main code visible right at the top of the file


## Scope
* Variables that we define are `scoped` to a specific function
* Variables defined outside any function are known as `global` variables and are accessable anywhere
* Variables defiend inside a function are only avaliable inside that function
```python
def test1():
	x = 10
	test2()

def test2():
	return x + 1 # causes an error

test1()
```
