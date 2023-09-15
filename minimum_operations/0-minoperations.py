#!/usr/bin/python3
"""
This module provides a function to calculate the
minimum number of operations to get 'n' H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly 'n' H characters in the file.
    Args:
        n (int): The target number of H characters.
    Returns:
        int: The minimum number of operations needed to reach 'n' H characters. 
        If
        'n' is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
