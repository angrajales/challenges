# The problem
Given a set of <b>n</b> players and a non negative integer <b>d</b>, find all pairs of players whose height in inchs adds <b>d</b>.

# The solution

Keep a dictionary with all previous heights, so if I analyze height of player <b>i</b> then I search for all previous players whose height plus the current player height is equal to <b></d>, i.e. heights[<b>i</b>] + heights[j, j < <b>i</b>] = d.

# How to execute

## Execute main program

```
python main.py <total_inches>
```
<b>total_inches: </b> Non negative integer

## Execute some unit tests

```
python -m unittest main_test.py
```
## Sample execution

```
python main.py 139
```

## Sample execution output
```
Nate Robinson Brevin Knight
Mike Wilks Nate Robinson
```