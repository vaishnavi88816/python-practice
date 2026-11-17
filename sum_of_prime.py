def sum_of_primes(n: int) -> int:
    """Calculates the sum of all prime numbers up to n (inclusive)

    using the Sieve of Eratosthenes algorithm.

    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return sum(num for num, prime in enumerate(is_prime) if prime)


if __name__ == "__main__":
    n = int(input("Enter the upper limit (n): "))
    print(f"Sum of prime numbers up to {n}: {sum_of_primes(n)}")
