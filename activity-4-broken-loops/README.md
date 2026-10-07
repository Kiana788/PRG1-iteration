# Activity 4: Broken loops

File: `broken_loops.py`

Three faults. Nothing crashes, nothing hangs, and every output looks plausible.

## Predict

Work out what each call **should** produce:

- `count_to(5)` should print the numbers 1 to 5.1, 2, 3, 4, 5.
- `total_of([12, 7, 19, 3])` should give the sum of those four numbers. 41 
- A courier gets three attempts to deliver a parcel. If nobody answers by the
  third, it goes back to the depot. The call supplies five days of no answer.
  Courier: after three no-answers, "Returned to depot", on the third attempt.

## Run

Execute it.

## Investigate

The first two faults announce themselves if you counted properly. The third does
not, and it is the important one.

- `count_to(5)` printed four numbers. Which end of the `range` is wrong?
count_to(5) printed 1, 2, 3, 4: four numbers. The stop end of the range is wrong. range(1, n) stops before n, so it should be range(1, n + 1).
- `total_of` returned 42. Add the four numbers yourself. What is the difference,
  and where did it come from?
  total_of returned 42 instead of 41. The difference is exactly 1, and it comes from total = 1 at the start. A running total must start at 0.
- `delivery_outcome` printed "Returned to depot", which is what you expected.
  **Count how many attempts it actually made before saying so.** Add a `print`
  inside the loop if that helps. Was it three?
  delivery_outcome said "Returned to depot" after making four attempts, not three. Adding a print inside the loop shows attempts counting 1, 2, 3, 4. The check if attempts &gt; 3 runs at the top of the fifth pass, after a fourth knock has already been counted and, in the story, made. The limit should stop the fourth attempt from ever happening.

## Fault log

You will fill in exactly this, marked, in Task 2 this afternoon.

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
#	What you saw	What was wrong	How you fixed it
1	count_to(5) printed 1 to 4, one short	| The range stop was excluded, so it stopped before 5	|	Changed range(1, n) to range(1, n + 1)
2	total_of returned 42 instead of 41 | The accumulator started at 1 instead of 0	|	Changed total = 1 to total = 0
3	"Returned to depot" after four attempts, not three |	The limit was checked after incrementing, so the fourth attempt went through	| Check the limit before counting the attempt: move the attempts &gt; 3 test above the increment, or test if attempts &gt;= 3: return "Returned to depot" before adding 1

## Modify

Fix all three. After fixing, `count_to(5)` prints 1 to 5, `total_of` returns 41,
and `delivery_outcome` gives up after the third attempt, not the fourth.

> The third fault is the one to remember. A courier making a fourth attempt when
> the contract allows three costs real money on every parcel, it produces exactly
> the message you expected, and no test you have not written will tell you about
> it. The same off-by-one on a limit turns up everywhere, including in Task 2.
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

(A simpler fix keeping the original shape: move if attempts &gt;= 3: return "Returned to depot" above attempts = attempts + 1. The key is that the check happens before the attempt is counted, so the fourth knock never occurs.)