'''
************Custom Character Counter*************

Write a python program that counts characters in a given file and print the stats in a log file.



************Problem Statement*************



Write a python program that takes filename as command line argument. If the filename is not given as command line argument the program should print exactly,



"""
Filename not provided.
Usage: python3 customCounter.py <file>
"""(without quotations)



The program should count occurrences of all the alphanumeric characters (i.e. A-Z, a-z, and 0-9) that are present in the file including common special characters belonging to [ `~!@#$%^&*()_+-=[]{}\|;'".>,</?]. Also the "A" and "a" are different characters, meaning the counting should be case sensitive. Once counting is done the program should output the stats (i.e. character and its count) in ":" separated form on standard output.

Print the output in the following order : a-z, A-Z, 0-9, special characters in the order given in the question.

Testrun Command: `python3 customCounter.py file1.txt` to test manually
Autograder: `python3 autograder.py` to test automatically

You can add more testcases and corresponding outputs in the testcases and expected_outputs folder respectively with the same name as the file name in the testcases folder. The autograder will automatically pick up the testcases and expected_outputs from these folders and run the tests.



************Example*************

Assume file1.txt has following text:

"""

Hello, I am Dheeraj
Nice to meet you

"""(without quotations)



Then the output should contain:



"""

a : 2
c : 1
e : 6
h : 1
i : 1
j : 1
l : 2
m : 2
o : 3
r : 1
t : 2
u : 1
y : 1
D : 1
H : 1
I : 1
N : 1
  : 6
, : 1


"""(without quotations)



Please note that "A" and "a" have 2 different entries, also " "(space) as a character is also part of the output. Please also note that any other characters other than given in the problem statement can be part of the testcases but they should not be considered in the counting





For command line argument handling, you will be required to use sys library. (It is already imported for you)

You can check these links to learn more about this library:

https://docs.python.org/3/library/sys.html

https://www.geeksforgeeks.org/python-sys-module/

'''
  
