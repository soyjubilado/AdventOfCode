## Things I learned during AoC 2024

  - Day 5: functools.cmp_to_key(), and using this with a closure.


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
    result in a fixed update. I was wrong.

    I used the rules to create a comparison function that I fed to sorted().
    This immediately solved the problem. It does depend heavily on a python
    library feature; I don't know how deeply I'd have to implement the same
    idea in another language: would I have to implement a sort algorithm?
    Implementing sort() isn't the worst thing in the world, but it's not the
    best either.

    The comparison function was created via a higher order function. Some
    part of this process is called a closure, but I'm not sure which.
