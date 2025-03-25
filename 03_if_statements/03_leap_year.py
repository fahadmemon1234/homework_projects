# -*- coding: utf-8 -*-
"""03_leap_year.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XrIfA1bMnodKCzdzQnlUWbT-Z8lZVlWh
"""

def main():

  year = int(input("Please input a year: "))

  if(year % 4 == 0):
    if(year % 100 == 0):
      if(year % 400 == 0):
        print("That's a leap year!")
      else:
        print("That's not a leap year.")
    else:
      print("That's a leap year!")
  else:
    print("That's not a leap year.")


if __name__ == '__main__':
    main()