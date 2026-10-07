# Activity 1: Counting

File: `counting.py`

## Predict

Three loops. For each one, write down **how many lines** it prints and **what
the first and last numbers are**. Do all three before running anything.
Loop	Lines	First	Last
range(5)	5	0	4
range(1, 6)	5	1	5
range(0, 10, 2)

## Run

Execute it.

## Investigate

- `range(5)` printed five numbers, and the last one was not 5. Where does it stop,
  and where does it start?
- `range(1, 6)` printed 1 to 5. Describe in one sentence what the two numbers in
  the brackets actually mean.
- `range(0, 10, 2)` has three numbers. What does the third one do?
- Predict, then check: how many lines does `range(10, 0, -1)` print?
range(5) starts with 0 (start value is not specified, so it is 0) and ends with 4 (before 5). There will be five numbers: 0, 1, 2, 3, 4.
In range(1, 6), the first number is the starting point of counting and it is included, while the second one is the ending and it is excluded. We count from 1 to 5.
The third number shows the step: how many to add each time. Thus, range(0, 10, 2) equals 0, 2, 4, 6, 8.
range(10, 0, -1) equals 10, 9, 8, 7, 6, 5, 4, 3, 2, 1. There will be 10 lines printed. The range ends with 0, but does not include it.
Change
Count from 1 to 5 without using range(1, 6): use range(5) and print i + 1:

## Modify

- Change the first loop so it counts 1 to 5 instead of 0 to 4, without using
  `range(1, 6)`.
Count 1 to 5 without range(1, 6): keep range(5) and print i + 1:
  for i in range(5):
    print(i + 1)

- Change the third loop to print the odd numbers below 10.
for i in range(1, 10, 2):
    print(i)
1, 3, 7, 9. the stop must be 10, not 9, because the stop is excluded.

> Getting the end of a `range` wrong by one is the single most common loop fault,
> and it produces output that looks almost right.
 