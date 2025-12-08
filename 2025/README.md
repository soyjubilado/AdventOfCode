## Things I learned during AoC 2025

  - Day 3: Recursion isn't always more succint.
  - Day 4: Easy isn't always clean.
  - Day 7: Using closures to avoid global variables. Also, some
    weird idiosyncracies with adding tuples to sets.

## Notes On Individual Days

### Day 1

  - Nice warmup, but part 2 had a gotcha: if you move the dial more than
    the size of the dial, you'll automatically pass 0.

### Day 2

  - Skipped day 2 due to a hangover. This probably shouldn't have happened,
    given that it was a Tuesday.

### Day 3

  - Fun recursion for part 2; I modified part 1 to use the same solution.

### Day 4

  - Used a grid library I wrote for previous years.


### Day 5

  - It's tempting to call your class "range." Don't do it.

### Day 6

  - Messy. It's all about parsing the input.

### Day 7

  - I thought I had a nice recursive solution for part 1, but it wasn't so
    nice after all. I needed to pass the whole grid in as an argument, but
    because it was a dictionary, and thus not hashable, I couldn't memoize
    the function using @lru_cache (still on python 3.8).

    The messy solution would have been to use grid as a global variable, which
    would have been appropriate for a program of this size. But I could avoid
    the global by using a closure; which I'm not sure is better than a
    global.

    For Part 2 I used the list of splitters from part 1, and I started with
    the bottom row. For each cell in the bottom row, how many paths could lead
    there? I'd move up one cell at a time, and stop when I ran out of space.
    Every time I passed a known splitter, I recursed to the spot above that
    splitter. Again, I used a closure to avoid global variables, and to be
    able to use @lru_cache.

### Day 8

  - This was, surprisingly, straighforward. I did check to see how many
    pairs of junction boxes I'd be dealing with. Given 1000 coordinates,
    there are roughly 500000 combinations of pairs. Iterating through all
    the pairs and calculating a distance took less than a second.

    Then I needed a way to keep track of the combined circuits. I used a
    dictionary keyed on the coordinates of all the boxes. So a dictionary of
    1000 coordinates, each one pointing to a set that included just itself.

    Then, every time two boxes were connected, the two sets were merged, and
    every key in the new merged set was updated.

    For part 2, I kept iterating until the resulting merged set had a size
    of 1000 (all the junction boxes).
