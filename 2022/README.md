## Things I learned during AoC 2022

  - Basic operations for git, including difftool.
  - Setting up a repository on github.
  - Python has set comprehensions. (day 3)
  - Using Python's built-in unittest. (day 3)
  - Brits call the game "Paper Scissors Rock."
  - If you nest iterators, there is an issue with not knowing where the
    `StopIteration` was raised. This will get caught by pylint, and refers to
    PEP-479. I eventually refactored to eliminate the nested iterators. (day
    10)
  - If you're looking for the shortest path, but the weights between vertices
    are always 1, then you don't need Dijkstra's algorithm, only BFS.
    Dijkstra's algorithm reduces to BFS in this case, but with the overhead of
    maintaining the priority queue. (day 12).
  - json.loads is a safe alternative to eval(). (day 13)
  - Python 3 got rid of cmp functions for sort, so you have to convert it
    to a key function via functools.cmp_to_sort(). (day 13)
  - Python has complex numbers, and these can be used to represent coordinates
    on a grid.

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

I used a tree. People who did it fast didn't use a tree. Maybe nested
dictionaries? I didn't implement it especially fast, but I didn't have to think
very hard.

- concepts: OOP, trees

### Day 8

Treehouses. Initially I wanted to look into the forest from every direction,
but that was a bad idea. Instead, look at every tree in the forest and see if
it is visible. You get all the trees between it and the edge in every
direction, and if the tallest tree in that direction is shorter than self, then
it's visible.  For part 2 I used an iterator and stepped through until I hit a
tall tree. Used a grid of coordinates for this even though I didn't need to.

- concepts: sets, min, max

### Day 9

Snake game! The grid of coordinates worked better for this problem because I
only kept the coordinates that the rope actually occupied.  To draw out the
grid, I figured out the min and max coordinates in each axis.

I got part 1, then went to bed. I did read on the forum what the most common
mistake was for part 2. Mulling it over in bed I was positive that my code
accounted for that. I was right, but I had an indentation error somewhere else
in the code. Brilliant.

I wrote the most unit tests for this one, they were easy to write.
However, I still managed
to break it when refactoring, even though the unit tests passed.
Added more unit tests.

- concepts: iterators

### Day 10

"The day of modulo arithmetic."

I was drunkest this day, couldn't finish even part 1 before going to bed.
Thought about it overnight, and used two iterators, one for the whole input
(that would repeat), and one for clock/register that would also go on forever.

- concepts: modulo  

### Day 11

Monkey business. More modulo! Were we prepped from yesterday?

This day evoked probably the biggest difference from the code that solved the
problem versus the code that I actually checked in.

I started when we got back from a Saturday night holiday party. I was not as
drunk as the previous night. I hardcoded the input into the first version.
Part 1 worked, but I was too sleepy to tackle part 2. I thought about it in bed
and figured it out, due partly to education. This day, I knew to stay away from
the forum until I solved the problem, because the trick would be in the
algorithm, not the implementation. Boy, was I right -- spoilers everywhere.

- concepts: modulo, lambda functions, function pointers

### Day 12

Path searching.

I borrowed code from last year's Day 15 for the shortest path algorithm.  I
continue to use a dictionary of grid coordinates to represent a two-dimensional
field.

Comments in the forum today pointed out that Dijkstra's algorithm is not
needed, since the cost between any two connected path points is always 1.
However, we didn't know that was going to be the case for Part 2 while we were
doing Part 1, so having a flexible algorithm is useful -- especially if I
already wrote it last year.

For Part 2, I just ran the Part 1 function from every possible starting point.
The function threw exceptions if I tried to start from
a location that had no solution. I just caught these exceptions and ignored
them. Someone noted that a more efficient algorithm would be to start and
the top and reverse the rule for descending the mountain until you reached
a low point.

I ended up writing a second version without Dijkstra's algorithm. It was
fairly simple to write, and it ran faster than the other version.

- concepts: Dijkstra's algorithm, BFS

### Day 13

Recursion: distress signal packets.

This was an especially fun day for me because I enjoy problems that have
recursive solutions. Although the input resembled the input from last year's
snailfish numbers puzzle (day 18), this one did not make me immediately think
I needed a parse tree. In fact, the representation was exactly the same as
a (nested) python list. So I warily read in the input via the python "eval"
function, only later learning that json.loads() is a safer option.

Although I was completely sober, I did not finish part 1 before bed. I did
think about it over night, though, and I knew where my bug was by morning.

For Part 2 I just used the function from Part 1 as the comparator function
for a python sort() of the input. The function needed only minor modifications.
Someone pointed out in the forum that you don't actually need to sort the
input -- you only need to know how many are lower than [[2]] and how many are
lower than [[6]]. That can be done in O(n).

Python 3 got rid of the cmp function for sort, so I needed
functools.cmp_to_key(func).

- concepts: recursion, eval(), json.loads, functools.cmp_to_key

### Day 14

Falling sand day.

Mostly straightforward. Good problem decomposition helps debugging. I added
an 'overlay' section to PrintGrid so that I could add the '+' to the
picture without modifying the grid.

- concepts: 2-d graphs

### Day 15

Sensors and beacons.

I wasn't even drunk, and I had a hard time understanding part 1. After writing
code to parse the input, I gave up and went to bed early. By morning, things
were more clear and I was able to code an inefficient solution to part 1. My
program took about 4 seconds on my actual input. I was storing the impossible
beacon locations individually, but I should have been storing them as ranges.

For part 2, I needed to rewrite the part 1 code to be more efficient. After I
finished this, part 1 completed in about 0.02 seconds.

Iterating over the millions of lines still took my program about 40 seconds
before finding a solution (after 3.2 million rows had been searched).

- concepts: big numbers?

### Day 16

Valves and tunnels (and elephants).

See comments at top of program. For part 1, I successfully reduced the problem
sufficiently so that an exhaustive search of all possible paths worked (in
under 5 seconds).

For part 2, partially based on a spoiler I read, I ran it twice: the first time
with the full set of targets for 26 seconds; then again with the list of
leftover targets, also for 26 seconds. This yielded the correct answer for my
data set, but I am certain that it wouldn't work for all datasets.

### Day 17

(skipped)

### Day 18

Part 1 was pretty straighforward -- just count the cubes, and subtract
shared sides.

For part 2, I thought build a box around the droplet and did a flood
fill to see how many sides are exposed on the outside.

Note: I had a bug in the first version of this that led me to believe it
wouldn't work, and so I wrote a version using a different algorithm. That
was the first version I checked in. However, I kept thinking about it, and
the numbers didn't add up, so I revisited the original algorithm and fixed
it. That is the current version. The bug was just due to sloppy programming;
a single unit test would have exposed it easily.

- concepts: neighbors in 3-d, flood fill

### Day 19

Still in progress.

### Day 20

Circular linked lists.

This was a pretty fun one. I created a Number class which held a value, and
a pointer to the next and previous value. When I instantiated each new object
and added it to the linked list, I also added the object to a regular python
list so I could keep track of the original order.

I knew there would be numbers, both negative and positive, that were
larger than the list itself, so I used the number modulo the length of the
list. The "fun" off by one errors kept happening because after you pull
the current number out of the list, the length of the list is shorter.

If Part 1 is done with an actual circular linked list, and the correct
modular arithmetic is applied, then Part 2 "just works" thanks to python's
handling of arbitrarily large numbers.

- concepts: circular linked list, modular arithmetic

### Day 21

Monkey arithmetic tree.

Building the tree was kind of fun, but probably unnecessary for part 1. 
Having the tree structure made for a pretty elegant general solution for
part 2.

For part 1, writing a recursive method for evaluating the value of a tree
branch was pretty easy. So the answer to part 1 was just calling this from
the top of the tree.

For part 2, I wrote a function to determine, given a node and a desired
value, return the node below it that led toward the humn node, and what
the value of that node had to be. It was less code than I expected, and it
was far more elegant than my original manual brute-force method for
finding the answer. I am most tickled by the fact that I have functions
called minuend, subtrahend, divisor, and dividend.

- concepts: tree data structures, recursion, arithmetic

### Day 22

Data were corrupted by my scraping program; leading spaces were stripped
on the first line.

I finally finished part 2 on January 8. There was a tiny bug that I couldn't
find until I solved the general case. After I solved the general case, I could
compare my output against the sample, and I figured it out. The bug was that
if the next spot went around a corner but was blocked by a '#', I retained
the orientation of the next spot, which I shouldn't have.

Solving the general case was another example of "I have no idea how to
tackle this." But I just went ahead and did what I could, starting with one
step that I knew I needed, being able to identify the edges of the shape.
Writing the solution for the general case was pretty challenging.

### Day 23

No quite cellular automata. Part 1 runs very quickly (10 rounds) but
Part 2 is somewhat slow for 900+ rounds. I may revisit this
code to look for improvements, but at least I knew not to represent the
white space. I did check that the rounds themselves are not getting
slower -- they shouldn't be.

- concepts: Don't store the whole grid.

#### Day 24

BFS with a constantly changing map.

Longer and probably slower than it needs to be. Create a blizzard class, and
a dictionary holding all the locations of blizzards. Every iteration, update
this dictionary.

Create another dictionary with an explorer class. The explorer looks at the
storm dictionary to see where it can move at any given moment. If there are
multiple possibilities, it clones itself and goes to all of them.

Part 1 goes quickly. The return trip on part 2 is very slow.
The calculation of the blizzard locations should be cached, because
there are only a few hundred possibilities.
