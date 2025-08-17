# COMPLETED


def digitFifthPowers(n):
    """
    Takes an integer n and returns the sum of the fifth powers of each digit
    """

    total = 0
    for i in str(n):
        total += int(i)**5

    return total


def problem30():

    # Upper limit is 5 * 9**5
    limit = 5 * 9**5

    fifthDigitSums = []

    for i in range(2, limit+1):
        if digitFifthPowers(i) == i:
            fifthDigitSums.append(i)

    return sum(fifthDigitSums)

if __name__ == "__main__":
    print(digitFifthPowers(123))
    print(problem30())