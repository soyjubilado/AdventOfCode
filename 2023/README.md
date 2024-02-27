## Things I learned during AoC 2023

  - [i for i in my_str] will get flagged by pylint (day 7)
  - sys.setrecursionlimit(n) will change from the default 1000 (day 5)

## Notes On Individual Days

### Day 1

  - The infamous "eightwo" issue. I couldn't figure out part 2 without hint.

    My problem was that I had a neat, clean solution for part 1 that I
    wanted to reuse. So I thought that an easy way to do it would be to
    substitute strings in the input. The question was whether "eightwo"
    would translate to "8wo" or "eigh2"? So I wrote it both ways, figuring
    that one would be correct. But neither was. In fact, "eightwo" needs to
    translate to "82" in order to get the correct answer.

### Day 3

  - It is unusual for me to be using a custom class this early in the month.
    A "Number" class was useful to also keep track of neighboring cells. As
    usual, I used a dictionary to hold coordinates rather than any sort of
    array.

### Day 5

  - This was the worst. It took me over a week to do part 2. The lesson
    must be that if your solution is really long, there's a shorter way.
    I'm not sure I ever found the shorter way, but I did have two recursive
    functions just because they were shorter than the iterative route.

    I also went down a few wrong paths. I had a hard time wrapping my head
    around how I was going to split the ranges so that they didn't cross
    borders, but I was overcomplicating it. At one point I decided I needed
    three lists, one for start and end points per range, another for just
    the start points, and another for just the ends. Thankfully my final
    implementation did not include this.

### Day 7

  - I was happy that all of Part 1 was useful for Part 2.
    
    For part 2, I just replaced the 'J' in with the most common other card to
    determine the strength of the card. I retained the original hand for
    tiebreakers. There was no need to figure out which card to use if the
    hand was two pairs, because it doesn't matter in this game.

### Day 8

  - The input was crafted to allow a simple solution. I had mapped out
    a solution in my head, and I thought of a few scenarios where the general
    solution could be a little irksome. So I wrote a quick function to
    analyze the data, and the solution jumped out at me. I was actually
    able to get an answer using a calculator and the analysis.

    I called the linux "factor" command to help with the analysis.


### Day 9

  - Super fun and short if you use recursion. Probably still simple
    with an iterative solution, but maybe not as fun.


### Day 10

  - I wrote lots of little functions to make the program cleaner at
    the top level. Part 2 was somewhat challenging both in designing
    an algorithm and implementing it. A simple flood fill would
    obviously not work.

    My approach was to traverse the path, and at each step there is
    a side on the left of the traversal, and a side on the right. At
    each step, I'd move leftward and rightward from the path until I
    hit the end of the world, or another cell in the path. I'd collect
    all the points along the way. At the end, I would have a collection
    of points on the 'left' side of the path, and another for the
    'right' side of the path. One of those would be all the sought
    points of the interior.

### Day 11

  - Shortest time between Part 1 and Part 2 for me, due to spoilers in
    the memes.

### Day 12

  - I found this problem to be especially enjoyable. Part 1 went quickly
    using a brute force algorithm that I suspected would not be useful
    for part 2. Indeed, I was right.

    I spent about a week on part 2, trying out different approaches. The
    initial approach was to leverage methodology from part 1 but by
    reducing the search space. I split the spring into subsprings, each
    subspring separated by one or more '.' and then tried the original
    brute force method. The first few lines were solved fairly quickly,
    but then it slowed down from there. I thought I'd let it run overnight,
    but after less than an hour my computer froze and had to be rebooted.

    I've never knowingly used dynamic programming on any AOC problem,
    but I use recursion a lot. By the end I had a good solution that was
    still too slow. As soon as I memoized the recursive function, the
    program was able to complete.
  
### Day 13

  - I spent a lot of time writing tests for this problem.
  
    When stuck, it's good to look at the output for the individual
    cases -- there were some grids where no reflection was found, and my
    function just returned 0 and kept going.
    
    Reading the forum sent me on a wild goose chase. The only reflections
    were like those in the examples; ie reflections only existed between
    rows and columns, so two consecutive identical rows or columns were a
    good candidate for a line of reflection.
    
    I was thwarted in part 2 because my function from part 1 assumed that
    there would be only one valid reflection, and it cut out as soon as it
    found that one. For part 2, it was possible that there would be two
    valid reflections, and one had to identify the *new* one.
    
    I wrote a class GridWrap as a wrapper around the grid dictionary because
    I wanted some way to abbreviate the output for my unit tests.
    
    This problem took me about 3 days to solve both parts.


### Day 14

  - This problem was relatively straightforward, since I re-used the grid
    representation from previous problems.
    
    My first implementation of TiltNorth() was very slow because I iterated
    through the whole map, and if I found a round rock I tried to move it one
    space. If there was any movement after iterating through all the spots,
    then I repeated. Part 1 took about 5 seconds in this implementation. After
    I rewrote the function for Part 2, Part 1 ran in 0.03 seconds.
    
    The rewrite for Part 2 logically approached one column at a time, iterating
    the column from top to bottm and sliding every free rock as far north as
    it could go. That algorithm was *O*(width of grid).

    I was especially happy with my DRY implementation of the TiltRocks()
    function called by TiltNorth(), TiltWest(), etc.

    It was tempting to just solve Part 2 by figuring out the cycle manually,
    but coding a generic solution didn't take too long. There are some magic
    numbers in the code because there's no way to guess where the cycle would
    start without a little trial and error.

### Day 15

  - Nothing especially difficult here except reading instructions.
