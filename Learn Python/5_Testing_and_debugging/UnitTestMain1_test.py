from UnitTestMain1 import *

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

"""OUTPUTS
---------------------------------
Inputs: 1, 200
Expecting: 300
Actual: 300
Pass
---------------------------------
Inputs: 2, 50
Expecting: 250
Actual: 250
Pass
---------------------------------
Inputs: 0, 0
Expecting: 0
Actual: 0
Pass
---------------------------------
Inputs: 0, 200
Expecting: 200
Actual: 200
Pass
---------------------------------
Inputs: 176, 350
Expecting: 17950
Actual: 17950
Pass
---------------------------------
Inputs: 250, 100
Expecting: 25100
Actual: 25100
Pass
============= PASS ==============
6 passed, 0 failed
[Finished in 238ms]
"""