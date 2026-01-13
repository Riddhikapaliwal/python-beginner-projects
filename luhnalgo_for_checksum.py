def luhn_check(number: str) -> bool:
# this algorithm is one of checksum algo....that is to varify if the given  unique number is correct or not.
    total = 0
    reverse_digits = number[::-1]

    for i, digit in enumerate(reverse_digits):
        d = int(digit)

        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9

        total += d

    return total % 10 == 0

card_number = "4532015112830366"

if luhn_check(card_number):
    print("Valid card number")
else:
    print("Invalid card number")
