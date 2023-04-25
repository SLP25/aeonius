import os
import filecmp
from aeonius_parser import parse

def test(file):
    
    with open(f"tests/input/{file}") as f:
        input = f.read()

    with open(f"tests/output/{file}") as f:
        expected = f.read()

    return parse(input) == expected

input_files = set(os.listdir("tests/input/"))
output_files = set(os.listdir("tests/output/"))

if input_files != output_files:
    print("[WARN] Different files in input and output folder. Using only common elements")

files = input_files.intersection(output_files)

passed = 0
not_passed = 0

for file in files:
    if test(file):
        passed += 1
    else:
        not_passed += 1

print("=============================")
print("=         SUMMARY           =")
print("=============================")
print(f"{passed} tests passed")
print(f"{not_passed} tests failed")
