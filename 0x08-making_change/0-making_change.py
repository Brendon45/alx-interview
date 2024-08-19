#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    Dynamic Programming Bottom-Up Solution.

    Args:
    coins (list): List of coin denominations.
    total (int): The target amount to achieve with the fewest coins.

    Returns:
    int: The fewest number of coins needed to achieve the total.
         Returns -1 if the total cannot be met with the given coins.
    """

    # If the total is 0 or less, no coins are needed.
    if total <= 0:
        return 0

    # If the coins list is empty or None, it's impossible to make any total.
    if coins == [] or coins is None:
        return -1

    # Check if there's an exact match for the total in the coins list.
    # If so, we only need 1 coin.
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass  # If total is not in the coins list, proceed to the next steps.

    # Sort the coins in descending order.
    coins.sort(reverse=True)

    # Initialize the coin count to keep track of the number of coins used.
    coin_count = 0

    # Iterate through each coin in the sorted list.
    for i in coins:
        # If the total is divisible by the coin value, use as many as needed.
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count

        # If the coin can be used to reduce the total:
        if total - i >= 0:
            # Use as many of this coin as possible.
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i  # Update total to the remainder.
            else:
                # Use one coin and reduce the total.
                coin_count += 1
                total -= i
                # If the total becomes 0, break out of the loop.
                if total == 0:
                    break

    # If total remains, it's impossible to meet.
    if total > 0:
        return -1

    # Return the total number of coins used.
    return coin_count
