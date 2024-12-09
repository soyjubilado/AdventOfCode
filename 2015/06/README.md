### Day 6

#### Part 1

Part 1 is done with sets. I keep a set of all the lights that are turned on. For every line in the input, add to the set or take away from the set depending on the operation. "On" is set.union; "off" is set.difference; and "toggle" is set.symmetric_difference, sort of like XOR.

#### Part 2

Part 2 is done in the obvious way. I have a dictionary of all the lights that are on. The next "on" operation will turn up the brightness by 1, or by 2 if it's a "toggle" operation. "Off" will decrement brightness, and if it reaches zero then that light is removed from the dictionary. 
