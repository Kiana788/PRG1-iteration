def count_to(n):
    for i in range(1, n + 1):
        print(i)


def total_of(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def delivery_outcome(door_log):
    attempts = 0
    for knock in door_log:
        if attempts &gt;= 3:
            return "Returned to depot"
        if knock == "answered":
            return f"Delivered on attempt {attempts + 1}"
        attempts = attempts + 1
    return "Ran out of days"
