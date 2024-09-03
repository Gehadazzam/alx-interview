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
    def sieve_of_eratosthenes(max_n):
        """
        Generate a list indicating whether numbers up to max_n are prime.
        
        Args:
        max_n (int): The maximum number to check for primes.
        
        Returns:
        list: A list where index i is True if i is a prime number, otherwise False.
        """
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False
        
        for i in range(2, int(max_n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, max_n + 1, i):
                    primes[j] = False
        
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i-1] + (1 if primes[i] else 0)

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if prime_count[n] % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
