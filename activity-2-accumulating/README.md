# Activity 2: Accumulating

File: `accumulating.py`

## Predict

- What does `total_of([12, 7, 19, 3])` return? total_of([12, 7, 19, 3]) returns 41 (12 + 7 = 19, + 19 = 38, + 3 = 41).
- What does `total_of([])` return? total_of([]) returns 0. The loop body never runs, so total is returned as it started.
- What does `largest_of([12, 7, 19, 3])` return? largest_of([12, 7, 19, 3]) returns 19.

## Run

Execute and compare.

## Investigate

- `total` starts at 0. Trace what it holds after each pass of the loop. Write the
  four values down.Trace of total: starts 0; after each pass: 12, 19, 38, 41.
- What would `total_of([12, 7, 19, 3])` return if `total` started at 1 instead? If the total had been initialized to 1, the outcome would have been 42, which is precisely one higher than the actual total. The error does not raise an alarm since a valid number is generated. 
  Predict the exact number, then try it.
- `largest_of` starts `biggest` at `numbers[0]` rather than at 0. Why? What would go wrong with a starting value of 0 if every reading were negative?
 Biggest always starts at numbers[0], therefore, the comparisons are always done with actual values in the list. However, if biggest started at 0 and all readings are negative, none of the readings can ever beat 0, leading to an erroneous output of 0 and numbers[0] will never be considered as a contender.
- `total_of([])` returns 0 without any special handling. Does `largest_of([])` behave as well? 
 Try it and see what happens.No, largest_of([]) causes an error of IndexError on numbers[0]. There is no first element to start with. While the sum starts off with zero, a largest so far does not.

## Modify

- Change `total_of` so it adds up only the numbers above 10.
def total_of(numbers):
    total = 0
    for number in numbers:
        if number > 10:
            total = total + number
    return total
Returns 31 for the readings: 12 + 19.)
smallest_of: change biggest = numbers[0] to stay (it does not change), change &gt; to &lt;, and rename for clarity:  

- Change `largest_of` into `smallest_of`. Which parts have to change, and which
  do not?
  def smallest_of(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number &lt; smallest:
            smallest = number
    return smallest
 comparison direction and names change.

> Where an accumulator starts is a decision, not a detail. Starting a total at 0
> and a maximum at the first item are both deliberate, and both go wrong quietly
> when copied to the wrong situation.
