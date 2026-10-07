# Activity 3: While, and stopping

File: `stopping.py`

## Predict

- What does `countdown(3)` print, line by line? countdown(3) prints 3, 2, 1, then "Liftoff" (four lines).
- What does `countdown(0)` print? Does the loop body run at all? countdown(0) prints only "Liftoff". The condition count &gt; 0 is false before the first pass, so the loop body never runs.
- What do the two `first_over` calls return? first_over(100, [45, 92, 130, 88]) returns 130. first_over(100, [45, 92, 88]) returns None, which prints as None.

## Run

Execute and compare. `countdown(0)` catches most people.

## Investigate

- `countdown` checks its condition **before** running the body. That is why
  `countdown(0)` behaves as it does. Explain it to your partner in one sentence.
- Delete the line `count = count - 1` and predict what happens. **Do not run it**
  until you have said out loud what you expect. Then run it, and press Ctrl+C to
  stop it.
  Since a while checks its condition even before its first pass, a condition that is already false results in no passes, not one.
Count = count – 1 results in an infinite loop: since count remains equal to 3, count &gt; 0 remains true and "3" will be printed forever unless you press Ctrl+C.
- `first_over` has two ways of finishing: it finds something, or it runs out.
  Which line handles each? What does it return when it runs out?
  There are two conditions in which first_over ends: the return statement in the if case deals with the case where there is one (the early termination approach), while the return None outside of the loop deals with the case where it runs out of numbers.
- Every loop has at least one way out. How many does `first_over` have, and how
  many does `countdown` have?
Two cases in which first_over ends: the early return or, failing that, when it loops to the end and returns None. In the case of countdown, there is one way out: the while condition becomes false (print("Liftoff") comes afterwards).

## Modify

- Rewrite `countdown` as a `for` loop with `range`. Which version reads better,
  and why?
  def countdown(start):
    for count in range(start, 0, -1):
        print(count)
    print("Liftoff")
everything about how many times it runs is on one line, and there is no separate counter to remember to update, so the infinite-loop fault is impossible.

- Change `first_over` so it returns how many readings it checked before finding
  one, rather than the reading itself.
keep a counter: add checked = 0 before the loop, add checked = checked + 1 as the first line of the body, and return checked in the if. It returns None (or 0, based on preference) when it runs out.
Make (stretch example) 
# Route 1: the temperature is above the limit, so we stop and report it early.
# Route 2: the readings ran out without ever going over, so we report None.
def first_hot(readings, limit):
    for reading in readings:
        if reading &gt; limit:
            return reading
    return None

## Make (stretch)

Optional. Only if you have finished everything above.

Write a loop with exactly two ways out, one of them early. Then write down, in a
comment above it, what each route means in plain English. If you cannot describe
both in a sentence each, the loop is probably doing too much.
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
How it meets the task requirements:

Exactly two ways to get out of it. The return statement is in the if block within the loop, and the other one comes right after the for loop ends.
One of the two exits comes early. One of the two gets out of the loop when a value is above the threshold; the other one happens naturally at the end of the loop.
The comment gives a brief explanation of each: "Found one, and here is where" and "Ran out, there was none." As both explanations fit into one sentence each, the loop has only one purpose.
to keep the enumerate version the same two paths apply, with return index + 1 being the early path.
> A loop you cannot see the exit from is a loop you do not understand yet. When
> you read one, find every route out before you do anything else.
