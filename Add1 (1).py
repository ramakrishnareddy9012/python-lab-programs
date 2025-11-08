# Program to form the greatest number from given set of numbers

def largest_number(nums):
    from functools import cmp_to_key

    # Custom comparator: decide order based on concatenation result
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Convert numbers to strings for concatenation
    nums = list(map(str, nums))

    # Sort using the custom comparator
    nums.sort(key=cmp_to_key(compare))

    # Join to form final number
    largest = ''.join(nums)
    return largest

# Example
numbers = [3, 0, 3, 5]
print("Greatest Number:", largest_number(numbers))
