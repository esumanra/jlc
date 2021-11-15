"""
INPUTS:
    input arrays is stored in txt file (TC's)

HOW TO RUN:
    python main.py < in.txt

TIME COMPLEXITY: O(N)
    As array is only traveresed once

SPACE COMPLEXITY: O(1)
    No new variables are created and elements are modified in-place

RESULTS:
in:  [23.0, 25.0, 50.0, 15.0, 42.0, 36.0, 46.0, 16.0, 38.0, 21.0]
out: [23.0, 50.0, 15.0, 42.0, 25.0, 46.0, 16.0, 38.0, 21.0, 36.0]

in:  [-3.0, 20.0, -30.0, 31.0, 76.0, 8.0, -40.0, 26.0]
out: [-3.0, 20.0, -30.0, 76.0, 8.0, 31.0, -40.0, 26.0]

in:  [-719.0, -41.1, 291.0, 999.0, -6.96]
out: [-719.0, 291.0, -41.1, 999.0, -6.96]
"""


def sort(input_array):
    for index in range(len(input_array) - 1):
        if index % 2 == 0:
            if not (input_array[index] < input_array[index + 1]):
                input_array[index], input_array[index + 1] = (
                    input_array[index + 1],
                    input_array[index],
                )
        else:
            if not (input_array[index] > input_array[index + 1]):
                input_array[index], input_array[index + 1] = (
                    input_array[index + 1],
                    input_array[index],
                )


for no_of_tests in range(int(input().strip())):
    _ = input()
    input_array = list(map(float, input().strip().split()))
    print()
    print(
        f"in:  {input_array}",
    )
    sort(input_array)
    print(f"out: {input_array}")  # as array is mutable it's modifed value is retained
