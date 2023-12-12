## Things I learned during AoC 2023

  - [i for i in my_str] will get flagged by pylint (day 7)

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

  - Incomplete! I have an idea how to do part 2, but I get tired every time
    I think of the implementation.

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

  - Still working on part 2

### Day 11

  - Shortest time between Part 1 and Part 2 for me, due to spoilers in
    the memes.
