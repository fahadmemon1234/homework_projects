# -*- coding: utf-8 -*-
"""06_is_odd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CJCydK-u55Tc8fKfkpNuh0LAzhGI7qeM
"""

def main():
    for i in range(10, 20):
      if(i % 2 == 0):
        print(f"{i} even", end=" ")
      else:
        print(f"{i} odd", end=" ")



if __name__ == '__main__':
    main()