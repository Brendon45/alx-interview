# 0x03. Log Parsing

## Algorithm

## Python

For the ``“0x03. Log Parsing”`` project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

## Concepts Needed:

1. __File I/O in Python:__

    - Understand how to read from sys.stdin line by line.
    - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
  
2. __Signal Handling in Python:__

    - Handling keyboard interruption (CTRL + C) using signal handling in Python.
    - [Python Signal Handling](https://docs.python.org/3/library/signal.html)
  
3. __Data Processing:__

    - Parsing strings to extract specific data points.
    - Aggregating data to compute summaries.
  
4. __Regular Expressions:__

    - Using regular expressions to validate the format of each line.
    - [Python Regular Expressions](https://docs.python.org/3/library/re.html)
  
5. __Dictionaries in Python:__

    - Using dictionaries to count occurrences of status codes and accumulate file sizes.
    - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  
6. __Exception Handling:__

    - Handling possible exceptions that may arise during file reading and data processing.
    - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

## Additional Resources

  - [Mock Technical Interview](https://www.youtube.com/watch?v=5dRTK-_Bzd0)

## Requirements

### General

  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly ``#!/usr/bin/python3``
  - A ``README.md`` file, at the root of the folder of the project, is mandatory
  - Your code should use the `PEP 8` style (version 1.7.x)
  - All your files must be executable
  - The length of your files will be tested using `wc`

# Tasks

__0. Log parsing__

Write a script that reads stdin line by line and computes metrics:

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size> (see input format above)
- Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405`and `500`
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: ``<status code>: <number>``
    - status codes should be printed in ascending order

Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.

    alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
    #!/usr/bin/python3
    import random
    import sys
    from time import sleep
    import datetime

    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
        ))
        sys.stdout.flush()

    alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    ^CFile size: 17146
    200: 4
    301: 3
    400: 4
    401: 2
    403: 6
    404: 6
    405: 4
    500: 4
    Traceback (most recent call last):
    File "./0-stats.py", line 15, in <module>
    Traceback (most recent call last):
      File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
      KeyboardInterrupt
    sleep(random.random())
      KeyboardInterrupt
      alexa@ubuntu:~/0x03-log_parsing$

__Repo:__

        GitHub repository: alx-interview
        Directory: 0x03-log_parsing
        File: 0-stats.py

## Explanation

1.

      #!/usr/bin/python3

- This is a shebang line that tells the system to use the Python 3 interpreter to run this script.

2.      """ Log parsing:

        A script that reads stdin line by line and computes metrics:

        Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        <status code> <file size> (if the format is not this one, the line
        must be skipped)
        After every 10 lines and/or a keyboard interruption (CTRL + C),
        print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order

        line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
        <status code>, <file size>]

        """

- This is a docstring that explains what the script does, the input format it expects, and the output it produces.

3. 

        import sys

- This imports the `sys` module, which provides access to system-specific parameters and functions.

4.  

        def printx(data, status):
            """ print the log """
            print("File size: {}".format(data))
            for key, value in sorted(status.items()):
                if value != 0:
                    print("{}: {}".format(key, value))

- This defines a function named `printx` that takes two arguments: `data` (the total file size) and `status` (a dictionary containing the count of different status codes). It prints the total file size and the count of each status code that is non-zero.

5. 

        status = {
            "200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}

- This initializes a dictionary named `status` with keys representing possible `HTTP status` codes and values set to 0, indicating the count of each `status code`.

6.

        counter = 0
        data = 0

- These lines initialize `counter` to 0, which will count the number of lines processed, and `data` to 0, which will hold the total file size.

7.

        try:
            for line in sys.stdin:

- This starts a `try` block to catch `KeyboardInterrupt` exceptions. The `for line in sys.stdin` loop reads each line from the standard input (stdin).

8.

        if counter == 10:
            printx(data, status)
            counter = 1
        else:
            counter = counter + 1

- If `counter` equals 10, it calls the `printx` function to print the metrics and resets `counter` to 1. Otherwise, it increments `counter` by 1.

9. 

        parsed = line.split()

- This splits the current line into a list of strings, parsed.

10.

        try:
            data = data + int(parsed[-1])
        except Exception as e:
            pass

- This tries to add the last element of `parsed` (the file size) to `data`. If an exception occurs (e.g., if the last element is not an integer), it is caught and ignored.

11. 

        try:
            for key, value in status.items():
                if key == parsed[-2]:
                    status[key] = status[key] + 1
        except Exception as e:
            pass

- This loop iterates through the `status` dictionary. If the second-to-last element of `parsed` matches a key in `status`, it increments the corresponding value in `status`. If an exception occurs (e.g., if the second-to-last element is not a valid status code), it is caught and ignored.

12.

        printx(data, status)
       except KeyboardInterrupt as e:
           printx(data, status)

- After the loop ends (either normally or due to a `KeyboardInterrupt`), it calls `printx` to print the final metrics.

- In summary, this script reads log lines from `stdin`, calculates the `total file size`, `counts the occurrences of specific HTTP status codes`, and prints the results every 10 lines or when interrupted by the user.
