#!/usr/bin/python3

"""
This module provides a function to determine the winner of a game played between
Maria and Ben. The game involves choosing prime numbers from a set of consecutive
integers and removing the chosen number and its multiples from the set.

The function isWinner takes the number of rounds and an array of integers as input
and returns the name of the player who won the most rounds. If the winner cannot be
determined, it returns None.
"""

def isWinner(x, nums):
    """
    Determine the winner of a game played between Maria and Ben.

    Args:
    x (int): The number of rounds.
    nums (list): A list of integers representing the set of consecutive integers
                 for each round.

    Returns:
    str: The name of the player who won the most rounds, or None if the winner
         cannot be determined.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """
        Play a round of the game.

        Args:
        n (int): The set of consecutive integers for this round.

        Returns:
        str: The name of the player who won this round.
        """
        numbers = list(range(1, n + 1))
        player_turn = "Maria"
        while numbers:
            for num in numbers:
                if is_prime(num):
                    numbers = [n for n in numbers if n % num != 0]
                    player_turn = "Ben" if player_turn == "Maria" else "Maria"
                    break
            else:
                break
        return player_turn

    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_game(n)
        if winner:
            wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None

