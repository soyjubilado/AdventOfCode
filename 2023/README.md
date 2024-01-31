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

  - part 1 done
