# 2018 Day 2 Notes

AKA, fun with list comprehensions!

The first list comprehension is used to slurp the list of box IDs from the puzzle input:

```python3
box_ids = list(line.strip() for line in inputfile.readlines())
```

This one is pretty straightforward as far as list comprehensions go: for every line in the inputfile, run the `strip()` method on it.

The solution for part two of this puzzle utilizes two list comprehensions.

```python3
# solve part two
seen_ids = []
for box_id in box_ids:
    for seen_id in seen_ids:
        differences = sum(1 for a, b in zip(box_id, seen_id) if a != b)
        if differences == 1:
            common_letters = "".join(list(a for a, b in zip(box_id, seen_id) if a == b))
            print(f"Common letters between the correct box IDs: {common_letters}")
    seen_ids.append(box_id)
```

The first is used to calculate the number of differing characters between two given strings, `box_id` and `seen_id`.

```python3
differences = sum(1 for a, b in zip(box_id, seen_id) if a != b)
```

Let's break this down, shall we?

`zip()` aggregates elements from each iterable passed into it.

```python3
>>> list(zip('abc', '123'))
[('a', '1'), ('b', '2'), ('c', '3')]
```

List comprehensions let us use a `for` loop over the tuples returned by `zip(box_id, seen_id)` to check if the characters are different. If they are, a `1` is returned.

```python3
>>> list(1 for a, b in zip('rmyxua', 'rjyxga') if a != b)
[1, 1]
```

Then the `sum()` built-in function is used to add up the `1` values, which results in the total number of differing characters.

```python3
>>> sum(1 for a, b in zip('rmyxua', 'rjyxga') if a != b)
2
```

A similar list comprehension is used to find the characters common to the two given strings `box_id` and `seen_id`.

```python3
common_letters = ''.join(list(a for a, b in zip(box_id, seen_id) if a == b))
```

I'll leave the breakdown of this one as an exercise for the reader.


