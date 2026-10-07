def countdown(start):
    count = start
    while count > 0:
        print(count)
        count = count - 1
    print("Liftoff")


def first_over(limit, readings):
    for reading in readings:
        if reading > limit:
            return reading
    return None


countdown(3)
countdown(0)

print(first_over(100, [45, 92, 130, 88]))
print(first_over(100, [45, 92, 88]))

def countdown(start):
    for count in range(start, 0, -1):
        print(count)
    print("Liftoff")

def first_over(limit, readings):
    for index, reading in enumerate(readings):
        if reading &gt; limit:
            return index + 1
    return None

# Route 1: the temperature is above the limit, so we stop and report it early.
# Route 2: the readings ran out without ever going over, so we report None.
def first_hot(readings, limit):
    for reading in readings:
        if reading &gt; limit:
            return reading
    return None

# Route 1 (early): a reading above the limit is found, so the loop leaves at
# once with the position of that reading, counting from 1.
# Route 2 (end): the readings ran out with nothing above the limit, so the
# loop finishes normally and the position is None.
def position_over(limit, readings):
    checked = 0
    for reading in readings:
        checked = checked + 1
        if reading > limit:
            return checked
    return None


print(position_over(100, [45, 92, 130, 88]))   # 3
print(position_over(100, [45, 92, 88]))        # None
