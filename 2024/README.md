## Things I learned during AoC 2024

  - Day 5: functools.cmp_to_key(), and using this with a closure.
  - Day 9: heapify doesn't create a heap object -- the result is still
           a list, but one that works with heappush and heappop.


## Notes On Individual Days

### Day 1

  - Started late; took an hour. Stumbled on absolute values. Stumbled on
    strings vs ints. I guess I'm a little rusty.

### Day 3

  - I'm pretty adept at parsing strings, and I'm pretty bad at using regex.
    But when I saw the problem, I knew I would be better off learning regex
    than writing a parser.

    The python re.findall() function was especially useful for this problem.
    I don't recall having used it before, and it made regexes seem easy.

    Some people were tripped up by the input being multiline, but I went
    back to check the instructions, and there wasn't anything in there
    saying it was one line or many lines.

### Day 5

  - Part 1 was straighforward, but part 2 was exciting to figure out.
    I did not see
    an immediate way to get the update into the proper order, so when I went
    with every time a rule was broken, swap the two items that caused the
    rule to be broken. In my mind, repeatedly doing this would eventually
    result in a fixed update. I was wrong: while it worked for the example,
    it created an infinite loop on my input.

    I used the rules to create a comparison function that I fed to sorted().
    This immediately solved the problem. It does depend heavily on a python
    library feature; I don't know how deeply I'd have to implement the same
    idea in another language: would I have to implement a sort algorithm?
    Implementing sort() isn't the worst thing in the world, but it's not the
    best either.

    The comparison function was created via a closure. This was wholly
    unnecessary; I did it only to avoid a global variable.

### Day 6

  - More 2-dimensional grid work. In part 1, I included a fun method to
    visualize the traveler moving around the grid.

    For part 2, my initial thought was to look at all the spots on the
    path found in part 1, and at every spot drop an obstacle in front of
    it and start from there. However, the obstacle might have been
    encountered coming from a different direction first, so this yielded
    the wrong answer. Instead, I dropped an obstacle on every cell in the
    previous path, and started the traveler in the original location. This
    brute force method takes about 23 seconds.

    Loop detection was implemented using an exception, but there are lots
    of alternate ways to do it.

### Day 7

  - If you use a recursive solution, be sure to pop numbers from the right,
    due to the fact that the operators in the problem are always evaluated
    left to right.

    I got lucky and stumbled upon this very efficient solution just by
    chance.

### Day 9

  - Part 1 went by fast, but Part 2 stumped me with the implementation.
    The algorithm is spelled out in the problem statement.

    I probably optimized this solution more than necessary. It keeps an
    updated index of the leftmost space of size N, whereas it propbably
    would have been fine to just look for a big enough space every time
    I wanted to move a file.

### Day 11

  - The simplicity of the solution belies the effort put into it.

    Part 1 was super straightforward. I did it before bed last night.
    Part 2 was just 75 interations instead of 25. This wasn't going to
    work. I didn't calculate how big that array was going to be, but things
    got quite slow around 35 to 40 iterations.

    I did realize upon waking up that the trick was going to involve
    not writing out the whole solution, but just counting how large it
    was going to be.
