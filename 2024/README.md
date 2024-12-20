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

### Day 12

  - Many people solved this by counting corners. I counted actual edge
    pieces, and grouped together contiguous tiles.

### Day 13 Linear Algebra

  - I was not willing to re-learn matrix operations to solve a series of
    equations. I visualized a line going through the origin, and a line
    going through the prize. They interesected at a point; if that point
    could be reached by integer operations of pushing the button, then that
    claw machine could be solved.

### Day 14 (Spoilers)

  - The patten repeats after 10430 moves. The tree is symmetric, but not
    centered in any way. The tree does not comprise all the robots, just
    a bunch of them. It's pretty obvious when you look at it, but running
    it with a 0.2 second pause between images, you could miss it if you
    blink.

    After reading a little more about the problem, and other peoples'
    approaches, I liked the idea of calculating a score for the number of
    robots with N or more neighbors (I set N=2). Then iterate through all
    the pages until there is an outlier. For my dataset, if I keep going
    until there are at least 100 robots with 2 or more neighbors, that is
    the one with the tree. It takes about 90 seconds to iterate through
    some 7500 pages.

    This is the final version I've checked in, rather than the code that
    displays page after page hoping to see the tree.
 
### Day 15

  - I had fun doing the visualization for part 1. Part 2 is pending.

### Day 17

  - Pretty fun little assembly language puzzle. I knew part 1 would be
    enjoyable to implement, and I didn't really plan to do part 2 this late
    in the game; but I did play around with it just to see what was the
    magnitude of the answer. In doing so, I managed to solve the puzzle
    without writing much code.

    TODO: write an automated solution for part 2.

### Day 19

  - I read it and thought, isn't there a regex solution to this? So I tried,
    but the program would hang trying to evaluate it, so I gave up on that
    approach. Instead, I just used memoized recursion to look at all the
    different possibilities. Part 2 was so similar to part 1, I ended up
    deleting the code that was specific to part 1, and just using the one
    function for both parts.
