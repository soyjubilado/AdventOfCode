## AoC 2016

I started working on the 2016 puzzles in late 2022.

## Notes On Individual Days

### Day 7

Assuming that the brackets in the input all match, and no line starts
with a bracket, and brackets are not nested, I parsed the input by
replacing opening and closing brackets with spaces. Then I used the
string split() function to break up the line according to the words
outside and inside the brackets. Outside were the even indexes, and
inside were the odd indexes. This was much simpler than "real" parsing.
