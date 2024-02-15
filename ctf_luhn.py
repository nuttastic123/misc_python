
def luhn_verify(cardNo):

    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    # start from right of credit card number and decrement by -1 while nDigits > -1
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    # valid card is nSum / 10 is an integer
    if (nSum % 10 == 0):
        return True
    else:
        return False


def main():
    # we now have the start and end digits of the card just need to find the middle which will be from 0 to 9
    for i in range(5432100000001234, 5432109999991234, 10000):
        # each digit in a valid card in this case has the be a multiple of 123457
        if i % 123457 == 0 and luhn_verify(str(i)):
            print("CTFlearn{{{}}}".format(i))


if __name__ == "__main__":
    main()
