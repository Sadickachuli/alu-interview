#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations to get 'n' H characters.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly 'n' H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed to reach 'n' H characters. If 'n' is impossible to achieve, return 0.
    """

    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                break

        if dp[i] == float('inf'):
            dp[i] = i

    return dp[n]

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

