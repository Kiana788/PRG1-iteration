# Stretch 2: enumerate and zip

File: `pairing.py`

Optional. Only if you have finished the four core activities.

Two tools you will see in other people's loops long before you need to write
them yourself. Read them here so they are not a surprise later.

## Predict

Three blocks, separated by dashed lines. Write down the output of each before
running. The third block is the interesting one.

## Run

Execute and compare.

## Investigate

- `enumerate` gives you two things on each pass instead of one. What are they,
  and which one starts at 0? enumerate gives the index and the item on each pass. The index starts at 0.
- `zip` walks two lists together. What is the rule for what it pairs up?  zip pairs items position by position: first with first, second with second, and so on.
- The third block zips a list of two names against a list of three ages. It does
  not crash and it does not warn you. What happened to the third age? Why might
  that be a fault waiting to happen rather than a convenience? With a 2-name list zipped against a 3-age list, zip stops at the shorter list, so the age 35 simply disappears. No error, no warning. It is convenient when the lengths are meant to match, but if they are supposed to match and one is short, a silent truncation hides a data fault that a test should have caught.

## Modify

- Rewrite the first block using `range` and indexing instead of `enumerate`.
  Which version is easier to read, and which is easier to get wrong?
  First block with range and indexing:
  colours = ["red", "green", "blue"]
for index in range(len(colours)):
    print(f"{index}: {colours[index]}")
The enumerate version is easier to read and harder to get wrong; the range/index version has more moving parts (length, indexing, brackets) to mistype.
- Make the third block print something sensible about the age with no matching
  name, rather than silently dropping it.
  from itertools import zip_longest
for name, age in zip_longest(shortlist, ages, fillvalue="(no name)"):
    print(f"{name} is {age}")
This prints Alice is 25, Bob is 30, (no name) is 35. Alternatively, check lengths first:
if len(shortlist) != len(ages):
    print("Warning: lists are different lengths")

Prediction 1: Print one line, completed. The count begins at 5, therefore the count &lt; 3 statement is false right from the start, and the loop body will not execute at all. The while loop first checks then does something, therefore zero passes is a regular occurrence.
Prediction 2: Print three lines: 2, 5, 8. Begin at 2, step by 3, and stop before getting to 10 (which would have been the next number). The stop number is never reached.
> `zip` stopping at the shorter list is the behaviour people forget. If the two
> lists are supposed to be the same length, a silent truncation is exactly the
> kind of fault that survives testing.
