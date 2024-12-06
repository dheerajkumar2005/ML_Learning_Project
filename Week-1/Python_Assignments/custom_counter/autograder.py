import os
import subprocess

def run_test(test_file, expected_output_file):
    # Run the custom_counter.py script with the test file
    try:
        result = subprocess.run(['python3', 'custom_counter.py', test_file], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running custom_counter.py: {e}\n{e.stderr}")
        return False
    
    # Read the expected output
    with open(expected_output_file, 'r') as f:
        expected_output = f.read()
    
    # Compare the actual output with the expected output
    if result.stdout == expected_output:
        return True
    else:
        return False

def main():
    testcases_dir = 'testcases'
    expected_outputs_dir = 'expected_outputs'
    
    test_files = os.listdir(testcases_dir)
    expected_files = os.listdir(expected_outputs_dir)
    
    for test_file in test_files:
        expected_output_file = os.path.join(expected_outputs_dir, test_file)
        if os.path.basename(expected_output_file) in expected_files:
            if run_test(os.path.join(testcases_dir, test_file), expected_output_file):
                print(f'Test {test_file} passed.')
            else:
                print(f'Test {test_file} failed.')
        else:
            print(f'No expected output for {test_file}.')

if __name__ == '__main__':
    main()