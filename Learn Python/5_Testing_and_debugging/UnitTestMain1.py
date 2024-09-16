def total_xp(level, xp_to_add):
    total = level*100 + xp_to_add
    return total

"""Unit Tests
Up until this point, all the coding lessons you've completed 
have been testing you based on your code's console output 
(what's printed). For example, a lesson might expect your code 
(in conjunction with the code we provide) to print something like:

Armor: 2
Health: 18
Copy icon
If your code prints that exact output, you pass. If it 
doesn't, you fail.

A new type of lesson
Going forward, you'll encounter a new type of lesson: unit 
tests. A unit test is just an automated program that tests 
a small "unit" of code. Usually just a function or two. The 
editor will have tabs: the "main.py" file containing your 
code, and the "main_test.py" file containing the unit tests.

These new unit-test-style lessons will test your code's 
functionality rather than its output. Our tests will call 
functions in your code with different arguments, and expect 
certain return values. If your code returns the correct 
values, you pass. If it doesn't, you fail.

There are two reasons for this change:

It's more realistic. In the real world, you'll be writing
 unit tests and running them against your code to make 
 sure it works as expected.
You can run and debug your code with print statements, 
and leave those print statements in when you submit. 
Unlike the output-based lessons, you won't have to remove 
your print statements to pass.
*********************************************************************
ASSIGNMENT
Complete the total_xp function. It accepts two integers as input:

level
xp_to_add
There are 100 xp per level. total_xp should convert the 
current level to xp, then add this current xp to the xp_to_add 
argument and return the player's total xp. For example:

If a player is level 1 and gains 100 xp, they have 200 total xp.
If a player is level 2 and gains 250 xp, they have 450 total xp.
If a player is level 170 and gains 590 xp, they have 17590 total xp.
Tips
The pass keyword is a way to tell Python to do nothing. 
You'll need to replace it with your own code.
Take a look at the main_test.py file at the top of your 
editor. You can read the tests but you can't edit them.
If a lesson expects a returned value, make sure to always
 return a value, or else you may encounter some cryptic NoneType errors.
"""