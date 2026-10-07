# Stretch 1: Nested loops

File: `nested.py`

Optional. Only if you have finished the four core activities.

Nested loops are covered properly later in the module, with 2D data. This is a
first look, and the only question being asked is how many times things run.

## Predict

- How many lines does the multiplication table print, not counting the blank
  ones? Work it out, do not count the output. Table lines: 3 rows x 3 columns = 9 lines, not counting blanks.
- What is the final value of `total_printed`? outer runs 4 times, inner runs 2 times, so 4 x 2 = 8.

## Run

Execute and compare.

## Investigate

- The outer loop runs 3 times and the inner loop runs 3 times. The inner body
  runs 9. Where does 9 come from, and what would it be if the outer loop ran 5
  times and the inner ran 4? 9 comes from 3 x 3: for every pass of the outer loop, the inner loop runs completely, so the inner body runs outer-count times inner-count. Outer 5, inner 4 would give 20.
- The blank `print()` sits inside the outer loop but outside the inner one. How
  can you tell that from reading, and what would change if it were indented one
  level further?The blank print() is indented to the same level as for column, one level less than the print inside the inner loop, so it runs once per row rather than once per cell. Indent it one level further and you would get a blank line after every table line instead of one between rows.
- In the second example, `total_printed` is declared before both loops rather
  than inside either. What would happen if it were set to 0 at the top of the
  outer loop instead? Predict, then try it.If total_printed = 0 were moved inside the top of the outer loop, it would reset to 0 at the start of each row, and the final value would be 2 (the last inner count) instead of 8.

## Modify

- Change the table to go up to 5 by 5, and predict the new line count first.
5 by 5: change both ranges to range(1, 6). New line count: 5 x 5 = 25, plus blanks.
- Make the table print only the rows where `row` is even.
for row in range(1, 4):
    if row % 2 == 0:
        for column in range(1, 4):
            print(f"{row} x {column} = {row * column}")
        print()
