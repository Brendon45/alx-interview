# 0x05. N Queens

## Algorithm

## Python

The `“0x05. N queens”` project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

### Concepts Needed:

1. __Backtracking Algorithms:__

   - Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
   - [Backtracking Introduction](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)
  
2. __Recursion:__

    - Using recursive functions to implement backtracking algorithms.
    - [Recursion in Python](https://realpython.com/python-thinking-recursively/)
  
3. __List Manipulations in Python:__

    - Creating and manipulating lists, especially to store the positions of queens on the board.
    - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
  
4. __Python Command Line Arguments:__

    - Handling command-line arguments with the sys module.
    - [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)
  
By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

## Additional Resources

- [Mock Interview](https://www.youtube.com/watch?v=GneS80iYa7I)

## Requirements

## General 

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable

# Tasks 📃

## 0. N queens

![QUEENS](https://private-user-images.githubusercontent.com/125453474/302208613-43f48208-e42f-451a-b184-7c7d47c0793a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIyNDEyMTAsIm5iZiI6MTcyMjI0MDkxMCwicGF0aCI6Ii8xMjU0NTM0NzQvMzAyMjA4NjEzLTQzZjQ4MjA4LWU0MmYtNDUxYS1iMTg0LTdjN2Q0N2MwNzkzYS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzI5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcyOVQwODE1MTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNjI2MzU0MDFmMWMwNWI0NjI3MWUwMWMwZDMxODQzOTQ0NWIxYzVkNDYwNDUyNDliNzA0YzhiYTg5MmMwNmEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Ede_jcDh0SKcgnmDUeoeMtzXTy0CbeNKYtQWlS7M9yo)

Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
    - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
    - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
    - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
- You are only allowed to import the `sys` module

Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

      julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
      [[0, 1], [1, 3], [2, 0], [3, 2]]
      [[0, 2], [1, 0], [2, 3], [3, 1]]
      julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
      [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
      [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
      [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
      [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
      julien@ubuntu:~/0x08. N Queens$

__Repo:__

   - GitHub repository: `alx-interview`
   - Directory: `0x05-nqueens`
   - File: `0-nqueens.py`

