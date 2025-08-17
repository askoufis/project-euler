import math


def decimalToFactoradic(num, n):
    """
    Converts a decimal number into a factoradic number
    Input: The decimal number and the factoradic base n
    Output: A string representing the decimal number in base factorial
    """

    # I'd guess that a string uses less space than a list, but who knows with python
    factoradic = ""

    # Calculate the factoradic "bits" from left to right starting with the (n-1)! bit
    while n-1 > 1:
        factoradic += str(num // math.factorial(n-1))

        num = num % math.factorial(n-1)

        n -= 1

    # The second factoradic "bit" determines whether or not the number is odd or even
    # I took it out of the loop to avoid for some reason
    # Who knows
    factoradic += str(num % 2)

    # The first bit in base factorial will always be 0
    factoradic += "0"

    return factoradic


def factoradicToPermutation(factoradic, n):
    """
    Generates a permutation of the first n letters of the alphabet
    Input: The factoradic representation of the permutation (as a string of numbers) and the factoradic base n
    (an integer)
    Output: A string representing the permutation
    """

    # This is the ASCII value of 'a'. This will be used to generate the permutation
    start = 97

    permutation = ""

    elements = []

    # Generate a list containing the first n letters of the alphabet
    for i in range(n):
        elements.append(chr(start+i))

    for i in factoradic:
        permutation += elements.pop(int(i))

    return permutation


def permutationToFactoradic(permutation, n):
    """
    Takes a permutation of the first n letters of the alphabet and returns the factoradic representation of that
    permutation
    Input: A permutation string and n an integer
    Output: A string containing the factoradic representation of the permutation
    """

    # There's probably a faster way to do this than O(N^2)

    factoradic = ""

    c = 1

    while c <= n:
        for i in permutation:
            counter = 0
            for j in range(c, n):
                if i > permutation[j]:
                    counter += 1

            c += 1

            factoradic += str(counter)

    return factoradic

if __name__ == "__main__":
    print(decimalToFactoradic(999999, 10))
    print(factoradicToPermutation('2662512110', 10))
    print(permutationToFactoradic('chidjbfega', 10))