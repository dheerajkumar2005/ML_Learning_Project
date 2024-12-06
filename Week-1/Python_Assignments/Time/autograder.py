import os

if (os.system(f'python3 time.py > out.txt'))==0:
    if (os.system(f'diff -w out.txt expected_output.txt'))==0:
        print("Test case passed")
    else:
        print("Test case failed")
        print("Above shows the mismatches")
    
else:
    print("Check for syntax errors or any other errors")

os.system(f'rm out.txt')