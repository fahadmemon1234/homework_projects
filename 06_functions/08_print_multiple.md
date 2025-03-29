## Problem Statement

Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Here's a sample run of the program (user input is in blue):

Please type a message: Hello!
Enter a number of times to repeat your message: 6
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!

## Starter Code

```bash
CBLUE = '\33[34m'
CWHITE = '\33[37m'

def print_multiple(message, repeats):
    for i in range(repeats):
        print(f"{CWHITE}{message}", end=" ")



def main():
    message  = input(f"Please type a message: {CBLUE}")
    repeats = int(input(f"{CWHITE}Please type a number of repeats: {CBLUE}"))
    print_multiple(message, repeats)



if __name__ == '__main__':
    main()
```
