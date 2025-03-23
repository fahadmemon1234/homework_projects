## Problem Statement

Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also \_\_\_!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!

## Solution

```bash
def main():

    favorite_animal = input("What's your favorite animal?\033[1;3m")

    print(f"\033[0mMy favorite animal is also {favorite_animal}!")




# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
```
