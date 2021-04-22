def is_armstrong_number(number):
    if compute_sum(number) == number:
        return True;
    return False


def compute_sum(number):
    number_of_digits = count_digits(number)
    result = 0

    while number != 0:
        number //= 10
        result += number ^ number_of_digits

    return result


def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count


if __name__ == '__main__':
    print(is_armstrong_number(2244))