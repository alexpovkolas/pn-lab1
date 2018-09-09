def is_lucky(digits):
    str_digits = str(digits)
    half_length = len(str_digits) / 2
    sum1 = 0
    sum2 = 0
    index = 0

    for d in str_digits:
        sum1 += int(d) if index < half_length else 0
        sum2 += int(d) if index >= half_length else 0
        index += 1

    return sum1 == sum2


def get_nearest_lucky_ticket(digits):
    index = 0

    while True:
        next_up = digits + index
        next_down = digits - index
        if is_lucky(next_up):
            result = next_up
            break
        if is_lucky(next_down):
            result = next_down
            break
        index += 1

    return result


