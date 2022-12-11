## Things I learned during AoC 2022

  - How to use git, including difftool
  - How to set up a repository on github
  - Python has set comprehensions (day 3)
  - How to use Python's built-in unittest (day 3)
  - Brits call the game "Paper Scissors Rock"
  - If you nest iterators, there is an issue with not knowing
    where the `StopIteration` was raised. This will get caught by
    pylint, and refers to PEP-479. I eventually refactored to eliminate
    the nested iterators.

## Notes On Individual Days

### Day 4
  - Overlapping ranges
  - Nice problem decomposition for unit tests.

### Day 5
  - Moving pallets. part 1 and 2 are essentially the same, but you
    reverse the pallet before putting it on.
  - concepts: stacks.

### Day 6
  - This was the super easy day that lulled everyone into a false sense
    of security.

### Day 7

I used a tree. People who did it fast didn't use a tree. Maybe
nested dictionaries? I didn't implement it especially fast, but I
didn't have to think very hard.

- concepts: OOP, trees

### Day 8

Treehouses. Initially I wanted to look into the forest from every
direction, but that was a bad idea. Instead, look at every tree in
the forest and see if it is visible. You get all the trees between
it and the edge in every direction, and if the tallest tree in that
direction is shorter than self, then it's visible.
For part 2 I used an iterator and stepped through until I hit a tall
tree. Used a grid of coordinates for this even though I didn't need
to.

- concepts: sets, min, max

### Day 9

Snake game! The grid of coordinates worked better for this problem
because I only kept the coordinates that the rope actually occupied.
To draw out the grid, I figured out the min and max coordinates in
each axis.

I got part 1, then went to bed. I did read on the forum
what the most common mistake was for part 2. Mulling it over in bed I was
positive that my code accounted for that. I was right, but I had an
indentation error somewhere else in the code. Brilliant.

I wrote the most unit tests for this one, they were easy to write.
However, I still managed
to break it when refactoring, even though the unit tests passed.
Added more unit tests.

- concepts: iterators

### Day 10

"The day of modulo arithmetic."

I was drunkest this day, couldn't finish even part 1 before going to bed.
Thought about it overnight, and used two iterators, one for the whole input
(that would repeat), and one for clock/register that would also go on
forever.

- concepts: modulo  

### Day 11

Monkey business. More modulo! Were we prepped from yesterday?

This day evoked probably the biggest difference from the code that solved
the problem versus the code that I actually checked in.

I started when we got back from a Saturday night holiday party. I was not
as drunk as the previous night. I hardcoded the input into the first version.
Part 1 worked, but I was too sleepy to tackle part 2. I thought about
it in bed and figured it out, due partly to education. This day, I knew to
stay away from the forum until I solved the problem, because the trick would
be in the algorithm, not the implementation. Boy, was I right -- spoilers
everywhere.

- concepts: modulo, lambda functions, function pointers
